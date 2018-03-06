import math


class GameBar:
    def __init__(self, position, acceleration, max_speed, time_delta):
        self._position = position
        self._speed = 0
        self._acceleration = acceleration
        self._max_speed = max_speed
        self._time_delta = time_delta

    def get_position(self):
        return self._position

    def get_speed(self):
        return self._speed

    def set_speed(self, speed):
        self._speed = speed

    def get_acceleration(self):
        return self._acceleration

    def set_acceleration(self, acceleration):
        self._acceleration = acceleration

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        self._max_speed = max_speed


class Keeper(GameBar):
    """Konstanten"""
    NUMBER_OF_FIGURES = 1
    DISTANCE_FIGURES = 0
    MAX_POS_KEEPER = 242
    POSITION_ON_BAR = 219

    def __init__(self, acceleration, max_speed, time_delta):
        super().__init__(self.MAX_POS_KEEPER / 2, acceleration, max_speed, time_delta)

    def move_up(self):
        new_speed = self._speed + self._acceleration * self._time_delta
        if new_speed <= self._max_speed:
            new_position = self._position + self._speed * self._time_delta \
                       + 0.5 * self._acceleration * self._time_delta * self._time_delta
            if new_position <= self.MAX_POS_KEEPER:
                self._position = new_position
            else:
                self._position = self.MAX_POS_KEEPER
            self._speed = new_speed
        else:
            self._speed = self._max_speed
            new_position = self._position + self._speed * self._time_delta
            if new_position <= self.MAX_POS_KEEPER:
                self._position = new_position
            else:
                self._position = self.MAX_POS_KEEPER

    def move_down(self):
        new_speed = self._speed - self._acceleration * self._time_delta
        if new_speed >= - self._max_speed:
            new_position = self._position + self._speed * self._time_delta \
                           - 0.5 * self._acceleration * self._time_delta * self._time_delta
            if new_position >= 0:
                self._position = new_position
            else:
                self._position = 0
            self._speed = new_speed
        else:
            self._speed = - self._max_speed
            new_position = self._position + self._speed * self._time_delta
            if new_position >= 0:
                self._position = new_position
            else:
                self._position = 0

    def stop(self):
        self.set_speed(0)


class Strategy(Keeper):
    def __init__(self, acceleration, max_speed, time_delta):
        super().__init__(acceleration, max_speed, time_delta)

    def new_strategy_step(self, ball):
        if ball.get_angle() > math.pi < 2*math.pi:
            if round(self._position) == self.MAX_POS_KEEPER / 2:
                self.stop()
            elif self._position < self.MAX_POS_KEEPER / 2:
                self.move_up()
            elif self._position > self.MAX_POS_KEEPER / 2:
                self.move_down()

        else:
            if round(self._position) == ball.get_y_position():
                self.stop()
            elif self._position < ball.get_y_position():
                self.move_up()
            elif self._position > ball.get_y_position():
                self.move_down()
