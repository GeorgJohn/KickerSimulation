import math
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

    def move(self):
        self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * self.__time
        self.__new_y_pos = self.__yPos + math.cos(self.__angle) * self.__speed * self.__time

        self.ball_collision()
        self.__xPos = self.__new_x_pos
        self.__yPos = self.__new_y_pos
        self.__angle = self.__new_angle
        # print(self.__angle*180/math.pi)

    def ball_collision(self):
        retval = False

        if self.__new_x_pos > COURT_WIDTH - BALL_RADIUS:
            delta_t_collision = (COURT_WIDTH - BALL_RADIUS - self.__xPos) / \
                               (math.sin(self.__angle) * self.__speed)
            self.__new_angle = 2*math.pi - self.__angle
            self.__new_y_pos = self.__yPos + math.cos(self.__angle) * self.__speed * self.__time
            self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * delta_t_collision
            retval = True

        elif self.__new_x_pos < BALL_RADIUS:
            delta_t_collision = (BALL_RADIUS - self.__xPos) / \
                                (math.sin(self.__angle) * self.__speed)
            self.__new_angle = 2 * math.pi - self.__angle
            self.__new_y_pos = self.__yPos + math.cos(self.__angle) * self.__speed * self.__time
            self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * delta_t_collision
            retval = True

        if self.__new_y_pos > COURT_HEIGHT - BALL_RADIUS:
            delta_t_collision = (COURT_HEIGHT - BALL_RADIUS - self.__yPos) / \
                               (math.cos(self.__angle) * self.__speed)
            if math.pi - self.__angle < 0:
                self.__new_angle = math.pi + 2*math.pi - self.__angle
            else:
                self.__new_angle = math.pi - self.__angle
            self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * self.__time
            self.__new_y_pos = self.__yPos + math.cos(self.__angle) * self.__speed * delta_t_collision

            retval = True

        elif self.__new_y_pos < BALL_RADIUS:
            delta_t_collision = (BALL_RADIUS - self.__yPos) / \
                                (math.cos(self.__angle) * self.__speed)
            if math.pi - self.__angle < 0:
                self.__new_angle = math.pi + 2*math.pi - self.__angle
            else:
                self.__new_angle = math.pi - self.__angle
            self.__new_x_pos = self.__xPos + math.sin(self.__angle) * self.__speed * self.__time
            self.__new_y_pos = self.__yPos + math.cos(self.__angle) * self.__speed * delta_t_collision
            retval = True

        return retval

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
