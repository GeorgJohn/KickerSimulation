import math
import random
from src.Constant import *


class Ball:
    def __init__(self, x_pos, y_pos, z_pos, speed, angle, omega_z, time_delta):
        self.__pos = [x_pos, y_pos, z_pos]
        self.__new_pos = [x_pos, y_pos, z_pos]
        self.__angle = angle
        self.__new_angle = angle
        self.__speed = speed
        self.__omega = omega_z
        self.__time = time_delta

    def move(self, kicker, keeper):
        self.__new_pos[Coordinate.X] = self.__pos[Coordinate.X] + math.sin(self.__angle) * self.__speed * self.__time
        self.__new_pos[Coordinate.Y] = self.__pos[Coordinate.Y] + math.cos(self.__angle) * self.__speed * self.__time

        if COURT_WIDTH / 2 < self.__pos[Coordinate.X] < COURT_WIDTH - X_POSITION_HUMAN_KEEPER - FIGURE_WIDTH / 2 \
                and 0 < self.__angle < math.pi:
            keeper.game_bar_intersection(self)

        i = 0
        while i < 3 and not kicker.collision(self):
            i = i + 1

        new_speed_square = self.__speed * self.__speed - 2 * 0.15 * 9810
        if new_speed_square > 0:
            self.__speed = math.sqrt(new_speed_square)
        else:
            self.kick_off()

        self.__pos[Coordinate.X] = self.__new_pos[Coordinate.X]
        self.__pos[Coordinate.Y] = self.__new_pos[Coordinate.Y]
        self.__angle = self.__new_angle

    def kick_off(self):
        self.__new_pos[Coordinate.X] = COURT_WIDTH / 2
        self.__new_pos[Coordinate.Y] = COURT_HEIGHT / 2
        self.__new_angle = random.uniform(math.pi / 4, 3 * math.pi / 4)
        self.__speed = 1000

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
