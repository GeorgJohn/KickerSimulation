from src import Environment_Controller

env = Environment_Controller.EnvironmentController()

for i_episode in range(20):
    observation = env.reset()
    for t in range(1000):
        env.render()
        action = env.get_random_action()
        observation, reward, done = env.step(action)
        print(observation, reward)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            break
