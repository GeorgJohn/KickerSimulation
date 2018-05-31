from enum import IntEnum


class Observation:

    def __init__(self):
        self._state = []

    def update(self, kicker, ball, computer_gamer):
        self._state = [kicker.get_score(),
                       ball.get_x_position(), ball.get_y_position(), ball.get_angle(), ball.get_speed(),
                       computer_gamer.get_position()]

    def get_state(self):
        return self._state


class EnvironmentModel(Observation):

    def __init__(self):
        super().__init__()
        self.__observation = Observation()
        self.__reward = 0
        self.__done = False
        self.__enable_view = False

    def __calc_reward(self):
        self.__reward += 1

    def update(self, kicker, ball, computer_gamer):
        self.__observation.update(kicker, ball, computer_gamer)
        self.__calc_reward()

    def get_reward(self):
        return self.__reward

    def set_reward(self, reward):
        self.__reward = reward

    def get_state(self):
        return self.__observation.get_state()

    def get_done(self):
        return self.__done

    def set_done(self, boolean):
        self.__done = boolean

    def set_enable_view(self, boolean):
        self.__enable_view = boolean

    def get_enable_view(self):
        return self.__enable_view

    def get_observation(self):
        return self.__observation


class Action(IntEnum):
    NOOP = 0
    UP = 1
    DOWN = 2
