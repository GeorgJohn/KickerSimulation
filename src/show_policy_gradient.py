import tensorflow as tf
import numpy as np
import random
import pygame

from src import Environment_Controller as Env
slim = tf.contrib.slim


def epsilon_greedy_action(action_distribution, epsilon=1e-1):
    if random.random() < epsilon:
        return np.argmax(np.random.random(
           action_distribution.shape))
    else:
        return np.argmax(action_distribution)


def epsilon_greedy_action_annealed(action_distribution, percentage, epsilon_start=1.0, epsilon_end=1e-2):
    annealed_epsilon = epsilon_start*(1.0-percentage) + epsilon_end*percentage
    if random.random() < annealed_epsilon:
        return np.argmax(np.random.random(action_distribution.shape))
    else:
        return np.argmax(action_distribution)


class PGAgent(object):

    def __init__(self, session, state_size, num_actions, hidden_size_1, hidden_size_2, learning_rate=1e-3,
                 explore_exploit_setting='epsilon_greedy_0.05'):
        self.session = session
        self.state_size = state_size
        self.num_actions = num_actions
        self.hidden_size_1 = hidden_size_1
        self.hidden_size_2 = hidden_size_2
        self.learning_rate = learning_rate
        self.explore_exploit_setting = explore_exploit_setting

        self.build_model()
        # self.build_training()
        self.saver = tf.train.Saver()

    def build_model(self):
        with tf.variable_scope('pg-model'):
            self.state = tf.placeholder(shape=[None, self.state_size], dtype=tf.float32)
            self.h0 = slim.fully_connected(self.state, self.hidden_size_1, activation_fn=tf.nn.sigmoid)
            self.h1 = slim.fully_connected(self.h0, self.hidden_size_2, activation_fn=tf.nn.sigmoid)
            self.h2 = slim.fully_connected(self.h1, self.hidden_size_1, activation_fn=tf.nn.sigmoid)
            self.output = slim.fully_connected(self.h2, self.num_actions, activation_fn=tf.nn.softmax)

    def sample_action_from_distribution(self, action_distribution, epsilon_percentage):
        # Choose an action based on the action probability
        # distribution and an explore vs exploit
        if self.explore_exploit_setting == 'greedy':
            action = epsilon_greedy_action(action_distribution)
        elif self.explore_exploit_setting == 'epsilon_greedy_0.05':
            action = epsilon_greedy_action(action_distribution, 0.05)
        elif self.explore_exploit_setting == 'epsilon_greedy_0.25':
            action = epsilon_greedy_action(action_distribution, 0.25)
        elif self.explore_exploit_setting == 'epsilon_greedy_0.50':
            action = epsilon_greedy_action(action_distribution, 0.50)
        elif self.explore_exploit_setting == 'epsilon_greedy_0.90':
            action = epsilon_greedy_action(action_distribution, 0.90)
        elif self.explore_exploit_setting == 'epsilon_greedy_annealed_1.0->0.001':
            action = epsilon_greedy_action_annealed(action_distribution, epsilon_percentage, 1.0, 0.001)
        elif self.explore_exploit_setting == 'epsilon_greedy_annealed_0.5->0.001':
            action = epsilon_greedy_action_annealed(action_distribution, epsilon_percentage, 0.5, 0.001)
        elif self.explore_exploit_setting == 'epsilon_greedy_annealed_0.25->0.001':
            action = epsilon_greedy_action_annealed(action_distribution, epsilon_percentage, 0.25, 0.001)
        else:
            action = Env.Action.NOOP
        return action

    def predict_action(self, state, epsilon_percentage):
        action_distribution = self.session.run(self.output, feed_dict={self.state: [state]})[0]
        action = self.sample_action_from_distribution(action_distribution, epsilon_percentage)
        return action


def main():

    env = Env.EnvironmentController()
    state_size = 5
    num_actions = 3

    explore_exploit_setting = 'epsilon_greedy_annealed_1.0->0.001'

    with tf.Session() as session:
        agent = PGAgent(session=session, state_size=state_size, num_actions=num_actions, hidden_size_1=900,
                        hidden_size_2=900, explore_exploit_setting=explore_exploit_setting)

        agent.saver.restore(session, "/tmp/model.ckpt")
        print("Model restored.")

        session.run(tf.global_variables_initializer())

        state = env.reset()
        state = state[-5:]

        clock = pygame.time.Clock()

        running = True
        while running:

            action = agent.predict_action(state, 1.0)

            state, _, terminal = env.step(action)

            if terminal:
                state = env.reset()

            state = state[-5:]

            env.render()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            clock.tick_busy_loop(60)


main()
