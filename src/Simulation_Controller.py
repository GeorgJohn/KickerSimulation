import pygame
import random
import math
import time
from src.Constant import *
from src import Simulation_View
from src import Ball_Model
from src import SimpleHumanAI_Model

ball_start_pos_x = COURT_WIDTH / 2  # random.randint(20, Const.COURT_WIDTH - 20)
ball_start_pos_y = COURT_HEIGHT / 2  # random.randint(20, Const.COURT_HEIGHT - 20)  # Position wo der Ball startet
ball_start_pos_z = 0
ball_speed = 0.2 * 1000  # Geschwindigkeit in m/s
ball_angle = random.uniform(0,  2 * math.pi)  # 3/2 * math.pi + 0.1  #
ball_angle_speed = 1.0
time_delta = 1 / 60
acceleration_bar = 0.5 * 1000  # Beschleunigung in m/s^2
speed = 100  # Stangen maximal Geschwindigkeit in m/s

my_view = Simulation_View.View()
my_ball = Ball_Model.Ball(ball_start_pos_x, ball_start_pos_y, ball_start_pos_z, ball_speed, ball_angle,
                          ball_angle_speed, time_delta)

my_strategy = SimpleHumanAI_Model.Strategy(speed, time_delta)

running = True
while running:

    start_time = time.perf_counter()

    my_ball.move()

    my_strategy.new_strategy_step(my_ball)

    my_view.display_empty_screen()
    my_view.display_court_line()
    my_view.display_info()
    my_view.display_ball(my_ball)
    my_view.display_human_figures(my_strategy)

    time.sleep(SEC_PER_FRAME + start_time - time.perf_counter())

    pygame.display.flip()  # Fenster anzeigen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
