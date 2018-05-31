import pygame
import random
from src.Constant import *
from src import Simulation_View
from src import Kicker_Model
from src import Ball_Model
from src import ComputerKeeper_Model
from src import Environment_Model

KEEPER_START_POS = MAX_POS_KEEPER / 2
BALL_START_POS_X = COURT_WIDTH / 2
BALL_START_POS_Y = COURT_HEIGHT / 2
BALL_START_SPEED = 1.0 * 1000
BAR_SPEED = 1.0 * 500
TIME_STEP = 1 / 60


class EnvironmentController:

    def __init__(self):
        random.seed()
        self.env = Environment_Model.EnvironmentModel()
        self.kicker = Kicker_Model.Kicker(TIME_STEP)
        self.ball = Ball_Model.Ball(x_pos=BALL_START_POS_X, y_pos=BALL_START_POS_Y, speed=BALL_START_SPEED,
                                    angle=random.uniform(0, 1), time_delta=TIME_STEP)
        self.computer_keeper = ComputerKeeper_Model.ComputerKeeper(BAR_SPEED, TIME_STEP)
        self.view = Simulation_View.View()

    def reset(self):
        self.env.set_done(False)
        self.ball.kick_off()
        self.computer_keeper.set_position(KEEPER_START_POS)
        self.env.update(self.kicker, self.ball, self.computer_keeper)
        self.env.set_reward(0)
        return self.env.get_observation()

    def render(self):
        self.view.display_empty_screen()
        self.view.display_court_line()
        self.view.display_info()
        self.view.display_ball(self.ball)
        self.view.display_computer_figures(self.computer_keeper)
        self.view.display_score(self.kicker.get_score())

        pygame.display.flip()

    def step(self):
        self.ball.move(self.kicker, self.computer_keeper,  human_keeper=None)
        self.env.update(self.kicker, self.ball, self.computer_keeper)
        self.check_for_done()
        return [self.env.get_observation(), self.env.get_reward(), self.env.get_done()]

    def check_for_done(self):
        if self.ball.get_terminal():
            self.ball.kick_off()
            self.ball.set_terminal(False)
            self.env.set_done(True)
        else:
            self.env.set_done(False)



