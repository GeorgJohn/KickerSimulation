import pygame
from src.Constant import *


class View:
    def __init__(self):
        self.__disp_x_position = 0
        self.__disp_y_position = 0
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGH))
        pygame.display.set_caption('ProCK Simulation')

    def display_empty_screen(self):
        self.screen.fill(FIELD_COLOUR)

    def display_ball(self, _ball):
        pygame.draw.circle(self.screen, WITHE,
                           (((-1) * round(_ball.get_x_position()) + MARGIN_LEFT + COURT_WIDTH),
                            (round(_ball.get_y_position()) + MARGIN_TOP)), BALL_RADIUS)

    def display_human_figures(self, keeper):
        pygame.draw.rect(self.screen, DARK_BLUE,
                         [KEEPER_OFFSET_X, round(keeper.get_position()) + KEEPER_OFFSET_Y,
                          FIGURE_WIDTH, FIGURE_HEIGHT])

    def display_court_line(self):
        pygame.draw.circle(self.screen, WITHE, (600 + MARGIN_LEFT, 345 + MARGIN_TOP), COURT_LINE_POINT_RADIUS)
        pygame.draw.circle(self.screen, WITHE, (830 + MARGIN_LEFT, 345 + MARGIN_TOP), COURT_LINE_POINT_RADIUS)
        pygame.draw.circle(self.screen, WITHE, (370 + MARGIN_LEFT, 345 + MARGIN_TOP), COURT_LINE_POINT_RADIUS)
        pygame.draw.line(self.screen, WITHE, (600 + MARGIN_LEFT, 0 + MARGIN_TOP),
                         (600 + MARGIN_LEFT, 245 + MARGIN_TOP), COURT_LINE_THICKNESS)
        pygame.draw.line(self.screen, WITHE, (600 + MARGIN_LEFT, 445 + MARGIN_TOP),
                         (600 + MARGIN_LEFT, SCREEN_HIGH - MARGIN_BUTTON), COURT_LINE_THICKNESS)
        pygame.draw.rect(self.screen, WITHE, [-10 + MARGIN_LEFT, 145 + MARGIN_TOP, 290, 400], COURT_LINE_THICKNESS)
        pygame.draw.rect(self.screen, WITHE, [920 + MARGIN_LEFT, 145 + MARGIN_TOP, 290, 400], COURT_LINE_THICKNESS)
        pygame.draw.rect(self.screen, WITHE, [-10 + MARGIN_LEFT, 210 + MARGIN_TOP, 160, 270], COURT_LINE_THICKNESS)
        pygame.draw.rect(self.screen, WITHE, [1050 + MARGIN_LEFT, 210 + MARGIN_TOP, 160, 270], COURT_LINE_THICKNESS)
        pygame.draw.arc(self.screen, WITHE, [135 + MARGIN_LEFT, 245 + MARGIN_TOP, 200, 200],
                        5.2, 1.1, COURT_LINE_THICKNESS)
        pygame.draw.arc(self.screen, WITHE, [865 + MARGIN_LEFT, 245 + MARGIN_TOP, 200, 200],
                        2.05, 4.25, COURT_LINE_THICKNESS)
        pygame.draw.circle(self.screen, WITHE, (600 + MARGIN_LEFT, 345 + MARGIN_TOP), COURT_LINE_CIRCLE_RADIUS,
                           COURT_LINE_THICKNESS)

    def display_info(self):
        pygame.draw.rect(self.screen, WITHE, [0, 0, SCREEN_WIDTH, MARGIN_TOP])
        pygame.draw.rect(self.screen, WITHE, [0, SCREEN_HIGH - MARGIN_BUTTON, SCREEN_WIDTH, MARGIN_BUTTON])
        pygame.draw.rect(self.screen, WITHE, [0, MARGIN_TOP, MARGIN_LEFT, COURT_HEIGHT])
        pygame.draw.rect(self.screen, WITHE, [SCREEN_WIDTH - MARGIN_RIGHT, MARGIN_TOP, MARGIN_RIGHT, COURT_HEIGHT])
        pygame.draw.line(self.screen, BLACK, (MARGIN_LEFT - 2, MARGIN_TOP - 2),
                         (COURT_WIDTH + MARGIN_LEFT, MARGIN_TOP - 2), 2)
        pygame.draw.line(self.screen, BLACK, (MARGIN_LEFT - 2, SCREEN_HIGH - MARGIN_BUTTON),
                         (COURT_WIDTH + MARGIN_LEFT, SCREEN_HIGH - MARGIN_BUTTON), 2)
        pygame.draw.line(self.screen, BLACK, (MARGIN_LEFT - 2, MARGIN_TOP - 2),
                         (MARGIN_LEFT - 2, SCREEN_HIGH - MARGIN_BUTTON), 2)
        pygame.draw.line(self.screen, BLACK, (COURT_WIDTH + MARGIN_LEFT, MARGIN_TOP - 2),
                         (COURT_WIDTH + MARGIN_LEFT, SCREEN_HIGH - MARGIN_BUTTON), 2)
