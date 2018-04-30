import pygame
import random
from src.Constant import *
from src import Simulation_View
from src import Ball_Model
from src import Kicker_Model
from src import HumanKeeper_Model
from src.SimpleHumanAI_Controller import SimpleHumanAI
# from src import SimpleHumanAI_Model

random.seed()

ball_start_pos_x = COURT_WIDTH / 2  # random.randint(20, Const.COURT_WIDTH - 20)
ball_start_pos_y = COURT_HEIGHT / 2  # random.randint(20, Const.COURT_HEIGHT - 20)  # Position wo der Ball startet
ball_start_pos_z = 0
ball_speed = 1 * 1000  # Geschwindigkeit in m/s
ball_angle = random.uniform(math.pi / 4, - math.pi / 4)  # 3/2 * math.pi + 0.1  #
ball_angle_speed = 1.0
time_delta = 1 / 60
acceleration_bar = 2 * 1000  # Beschleunigung in m/s^2
speed = 500  # Stangen maximal Geschwindigkeit in m/s

clock = pygame.time.Clock()
my_view = Simulation_View.View()
my_ball = Ball_Model.Ball(ball_start_pos_x, ball_start_pos_y, ball_start_pos_z, ball_speed, ball_angle,
                          ball_angle_speed, time_delta)
my_kicker = Kicker_Model.Kicker(time_delta)
my_human_keeper = HumanKeeper_Model.HumanKeeper(speed, time_delta)
my_human_strategy = SimpleHumanAI()

running = True
while running:

    my_ball.move(my_kicker, my_human_keeper)
    my_human_strategy.new_strategy_step(my_human_keeper, my_ball)

    my_view.display_empty_screen()
    my_view.display_court_line()
    my_view.display_info()
    my_view.display_ball(my_ball)
    my_view.display_human_figures(my_human_keeper)
    my_view.display_score(my_kicker.get_score())

    clock.tick_busy_loop(60)

    pygame.display.flip()  # Fenster anzeigen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
