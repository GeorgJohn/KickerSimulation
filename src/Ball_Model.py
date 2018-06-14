import math
import random
from src.Constant import *


class Ball:
    def __init__(self, x_pos=0, y_pos=0, z_pos=0, speed=0.0, angle=0.0, omega_z=0.0, time_delta=0.0):
        self.__pos = [x_pos, y_pos, z_pos]
        self.__new_pos = [x_pos, y_pos, z_pos]
        self.__angle = angle
        self.__new_angle = angle
        self.__speed = speed
        self.__omega = omega_z
        self.__time = time_delta
        self.__terminal = False

    def move(self, kicker, computer_keeper=None, human_keeper=None):
        self.__new_pos[Coordinate.X] = self.__pos[Coordinate.X] + math.cos(self.__angle) * self.__speed * self.__time
        self.__new_pos[Coordinate.Y] = self.__pos[Coordinate.Y] + math.sin(self.__angle) * self.__speed * self.__time

        if human_keeper:
            human_keeper.check_for_interaction(self)
        if computer_keeper:
            computer_keeper.check_for_interaction(self)

        i = 0
        while i < 3 and not kicker.collision(self):
            i = i + 1

        self.__speed = self.__speed - 0.02 * 9810 * self.__time
        if self.__speed <= 0:
            self.set_terminal(True)

        self.__pos[Coordinate.X] = self.__new_pos[Coordinate.X]
        self.__pos[Coordinate.Y] = self.__new_pos[Coordinate.Y]
        self.__angle = self.__new_angle

    def kick_off(self):
        self.__pos[Coordinate.X] = self.__new_pos[Coordinate.X] = COURT_WIDTH / 2
        self.__pos[Coordinate.Y] = self.__new_pos[Coordinate.Y] = COURT_HEIGHT / 2
        self.__new_angle = random.uniform(- 0.2326, 0.2326)
        if self.__new_angle > 0:
            self.__angle = self.__new_angle = self.__new_angle - math.pi
        else:
            self.__angle = self.__new_angle = self.__new_angle + math.pi
        self.__speed = 500

    def get_x_position(self):
        return self.__pos[Coordinate.X]

    def get_y_position(self):
        return self.__pos[Coordinate.Y]

    def get_z_position(self):
        return self.__pos[Coordinate.Z]

    def get_new_x_position(self):
        return self.__new_pos[Coordinate.X]

    def set_new_x_position(self, pos):
        self.__new_pos[Coordinate.X] = pos

    def get_new_y_position(self):
        return self.__new_pos[Coordinate.Y]

    def set_new_y_position(self, pos):
        self.__new_pos[Coordinate.Y] = pos

    def get_new_z_position(self):
        return self.__new_pos[Coordinate.Z]

    def set_new_z_position(self, pos):
        self.__new_pos[Coordinate.Z] = pos

    def get_speed(self):
        return self.__speed

    def set_speed(self, speed):
        self.__speed = speed

    def get_angle(self):
        return self.__angle

    def get_new_angle(self):
        return self.__new_angle

    def set_new_angle(self, angle):
        self.__new_angle = angle

    def get_angular_speed(self):
        return self.__omega

    def get_terminal(self):
        return self.__terminal

    def set_terminal(self, boolean):
        self.__terminal = boolean
