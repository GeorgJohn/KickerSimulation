import math
from src.Constant import COURT_HEIGHT


class GameBar:
    def __init__(self, position, speed, time_delta):
        self._position = position
        self._next_position = -1
        self._speed = speed
        self._time_delta = time_delta

    def get_position(self):
        return self._position

    def get_max_speed(self):
        return self._speed

    def set_max_speed(self, speed):
        self._speed = speed


class Keeper(GameBar):
    """Konstanten"""
    NUMBER_OF_FIGURES = 1
    DISTANCE_FIGURES = 0
    MAX_POS_KEEPER = 242
    OFFSET_KEEPER = (COURT_HEIGHT - MAX_POS_KEEPER) / 2
    POSITION_ON_BAR = 219

    def __init__(self, speed, time_delta):
        super().__init__(self.MAX_POS_KEEPER / 2, speed, time_delta)

    def _new_desired_pos(self, desired_pos):
        if 0 <= desired_pos <= self.MAX_POS_KEEPER:
            self._next_position = desired_pos
            self._pos_next_time_step()

    def _pos_next_time_step(self):
        if self._next_position > self._position:
            new_position = self._position + self._speed * self._time_delta
        elif self._next_position < self._position:
            new_position = self._position - self._speed * self._time_delta
        else:
            new_position = self._next_position

        if new_position > self.MAX_POS_KEEPER:
            self._position = self.MAX_POS_KEEPER
        elif new_position < 0:
            self._position = 0
        else:
            self._position = new_position


class Strategy(Keeper):
    def __init__(self, speed, time_delta):
        super().__init__(speed, time_delta)

    def new_strategy_step(self, ball):
        if ball.get_angle() > math.pi < 2 * math.pi:
            self._new_desired_pos(self.MAX_POS_KEEPER/2)
        else:
            self._new_desired_pos(ball.get_y_position() - self.OFFSET_KEEPER)
