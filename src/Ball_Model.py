import math
import random
from src.Constant import *


class Ball:
    def __init__(self, x_pos, y_pos, z_pos, speed, angle, omega_z, time_delta):
        self.__xPos = x_pos
        self.__yPos = y_pos
        self.__new_x_pos = x_pos
        self.__new_y_pos = y_pos
        self.__new_angle = angle
        self.__zPos = z_pos
        self.__speed = speed
        self.__angle = angle
        self.__omega = omega_z
        self.__time = time_delta
        self.__ball_in_goal_area = False
        self.__goal_for_human = False
        self.__goal_for_AI = False
        self.__score = [0, 0]

    def move(self):
        self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * self.__time
        self.__new_y_pos = self.__yPos + math.cos(self.__angle) * self.__speed * self.__time

        self.ball_collision()
        self.__xPos = self.__new_x_pos
        self.__yPos = self.__new_y_pos
        self.__angle = self.__new_angle
        # print(self.__angle*180/math.pi)

    def ball_collision(self):
        new_pos_in_range = False
        i = 0

        while not new_pos_in_range:
            i = i + 1

            if not self.__ball_in_goal_area:
                if self.__new_x_pos > COURT_WIDTH - BALL_RADIUS:
                    if GOAL_BAR_POS + BALL_RADIUS < self.__new_y_pos < GOAL_BAR_POS + GOAL_SIZE - BALL_RADIUS:
                        x_pos_in_range = True
                        self.__ball_in_goal_area = True
                    else:
                        delta_t_collision = (COURT_WIDTH - BALL_RADIUS - self.__xPos) / \
                                            (math.sin(self.__angle) * self.__speed)
                        self.__new_angle = 2 * math.pi - self.__angle
                        self.__new_y_pos = self.__yPos + math.cos(self.__angle) * self.__speed * self.__time
                        self.__new_x_pos = (COURT_WIDTH - BALL_RADIUS + math.sin(self.__new_angle) * self.__speed
                                            * (self.__time - delta_t_collision))
                        x_pos_in_range = False
                elif self.__new_x_pos < BALL_RADIUS:
                    if GOAL_BAR_POS + BALL_RADIUS < self.__new_y_pos < GOAL_BAR_POS + GOAL_SIZE - BALL_RADIUS:
                        x_pos_in_range = True
                        self.__ball_in_goal_area = True
                    else:
                        delta_t_collision = (BALL_RADIUS - self.__xPos) / \
                                            (math.sin(self.__angle) * self.__speed)
                        self.__new_angle = 2 * math.pi - self.__angle
                        self.__new_y_pos = self.__yPos + math.cos(self.__angle) * self.__speed * self.__time
                        self.__new_x_pos = (BALL_RADIUS + math.sin(self.__new_angle) * self.__speed
                                            * (self.__time - delta_t_collision))
                        x_pos_in_range = False
                else:
                    x_pos_in_range = True

                if self.__new_y_pos > COURT_HEIGHT - BALL_RADIUS:
                    delta_t_collision = (COURT_HEIGHT - BALL_RADIUS - self.__yPos) / \
                                        (math.cos(self.__angle) * self.__speed)
                    if math.pi - self.__angle < 0:
                        self.__new_angle = math.pi + 2 * math.pi - self.__angle
                    else:
                        self.__new_angle = math.pi - self.__angle
                    self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * self.__time
                    self.__new_y_pos = (COURT_HEIGHT - BALL_RADIUS + math.cos(self.__new_angle) * self.__speed
                                        * (self.__time - delta_t_collision))
                    y_pos_in_range = False
                elif self.__new_y_pos < BALL_RADIUS:
                    delta_t_collision = (BALL_RADIUS - self.__yPos) / \
                                        (math.cos(self.__angle) * self.__speed)
                    if math.pi - self.__angle < 0:
                        self.__new_angle = math.pi + 2 * math.pi - self.__angle
                    else:
                        self.__new_angle = math.pi - self.__angle
                    self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * self.__time
                    self.__new_y_pos = (BALL_RADIUS + math.cos(self.__new_angle) * self.__speed
                                        * (self.__time - delta_t_collision))
                    y_pos_in_range = False
                else:
                    y_pos_in_range = True
            else:
                if self.__new_x_pos > COURT_WIDTH + BALL_RADIUS:
                    self.__goal_for_human = True
                    self.kick_off()
                    self.__ball_in_goal_area = False
                elif self.__new_x_pos < - BALL_RADIUS:
                    self.__goal_for_AI = True
                    self.kick_off()
                    self.__ball_in_goal_area = False
                else:
                    if self.__new_y_pos > GOAL_BAR_POS + GOAL_SIZE - BALL_RADIUS:
                        delta_t_collision = (GOAL_BAR_POS + GOAL_SIZE - BALL_RADIUS - self.__yPos) / \
                                            (math.cos(self.__angle) * self.__speed)
                        if math.pi - self.__angle < 0:
                            self.__new_angle = math.pi + 2 * math.pi - self.__angle
                        else:
                            self.__new_angle = math.pi - self.__angle
                        self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * self.__time
                        self.__new_y_pos = (GOAL_BAR_POS + GOAL_SIZE - BALL_RADIUS + math.cos(self.__new_angle)
                                            * self.__speed * (self.__time - delta_t_collision))
                    elif self.__new_y_pos < GOAL_BAR_POS + BALL_RADIUS:
                        delta_t_collision = (GOAL_BAR_POS + BALL_RADIUS - self.__yPos) / \
                                            (math.cos(self.__angle) * self.__speed)
                        if math.pi - self.__angle < 0:
                            self.__new_angle = math.pi + 2 * math.pi - self.__angle
                        else:
                            self.__new_angle = math.pi - self.__angle
                        self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * self.__time
                        self.__new_y_pos = (GOAL_BAR_POS + BALL_RADIUS + math.cos(self.__new_angle) * self.__speed
                                            * (self.__time - delta_t_collision))
                y_pos_in_range = True
                x_pos_in_range = True

            if y_pos_in_range and x_pos_in_range:
                new_pos_in_range = True

            # Wenn die schleife 3 mal durchlaufen wurde, davon ausgehen das der Ball klemmt
            if i >= 3 and not new_pos_in_range:
                self.__new_y_pos = self.__yPos
                self.__new_x_pos = self.__xPos
                new_pos_in_range = True

    def kick_off(self):
        if self.__goal_for_human:
            self.__score[1] = self.__score[1] + 1
        elif self.__goal_for_AI:
            self.__score[0] = self.__score[0] + 1
        self.__goal_for_human = False
        self.__goal_for_AI = False
        self.__new_x_pos = COURT_WIDTH / 2
        self.__new_y_pos = COURT_HEIGHT / 2
        self.__new_angle = random.uniform(0,  2 * math.pi)

    def get_x_position(self):
        return self.__xPos

    def get_y_position(self):
        return self.__yPos

    def get_z_position(self):
        return self.__zPos

    def get_speed(self):
        return self.__speed

    def get_angle(self):
        return self.__angle

    def get_angular_speed(self):
        return self.__omega

    def get_human_goal(self):
        return self.__goal_for_human

    def get_ai_goal(self):
        return self.__goal_for_AI

    def get_score(self):
        return self.__score
