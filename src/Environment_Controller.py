import pygame
import random
from src.Constant import *
from src import Simulation_View
from src import Kicker_Model
from src import Ball_Model
from src import ComputerKeeper_Model

KEEPER_START_POS = MAX_POS_KEEPER / 2
BALL_START_POS_X = COURT_WIDTH / 2
BALL_START_POS_Y = COURT_HEIGHT / 2
BALL_START_SPEED = 1.0 * 1000
BAR_SPEED = 1.0 * 500
TIME_STEP = 1 / 60


class Environment:

    def __init__(self):
        random.seed()
        self.kicker = Kicker_Model.Kicker(TIME_STEP)
        self.ball = Ball_Model.Ball(x_pos=BALL_START_POS_X, y_pos=BALL_START_POS_Y, speed=BALL_START_SPEED,
                                    angle=random.uniform(0, 1), time_delta=TIME_STEP)
        self.computer_keeper = ComputerKeeper_Model.ComputerKeeper(BAR_SPEED, TIME_STEP)
        self.view = Simulation_View.View()
        self.enable_view = False

    def reset(self):
        self.ball.kick_off()
        self.computer_keeper.set_position(KEEPER_START_POS)

    def render(self):
        self.enable_view = True


