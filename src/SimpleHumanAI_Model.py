import math
from src.Constant import*


class GameBar:
    def __init__(self, position, speed, time_delta):
        self._position = position
        self._next_position = -1
        self._speed = speed
        self._time = time_delta

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
    OFFSET_VIEW_KEEPER = (COURT_HEIGHT - MAX_POS_KEEPER) / 2
    POSITION_ON_BAR = 219

    def __init__(self, speed, time_delta):
        super().__init__(self.MAX_POS_KEEPER / 2, speed, time_delta)

    def _new_desired_pos(self, desired_pos):
        if 0 <= desired_pos <= self.MAX_POS_KEEPER:
            self._next_position = desired_pos
        elif desired_pos > self.MAX_POS_KEEPER:
            self._next_position = self.MAX_POS_KEEPER
        elif desired_pos < 0:
            self._next_position = 0

        self._pos_next_time_step()

    def _pos_next_time_step(self):
        if self._next_position > self._position + 5:
            new_position = self._position + self._speed * self._time
        elif self._next_position < self._position - 5:
            new_position = self._position - self._speed * self._time
        else:
            new_position = self._next_position

        if new_position > self.MAX_POS_KEEPER:
            self._position = self.MAX_POS_KEEPER
        elif new_position < 0:
            self._position = 0
        else:
            self._position = new_position

    def check_for_shoot(self, ball):
        retval = False
        x_distance = COURT_WIDTH - X_POSITION_HUMAN_KEEPER - FIGURE_WIDTH // 2 - ball.get_x_position()
        y_distance = self._position + self.POSITION_ON_BAR - ball.get_y_position()
        if math.sqrt(x_distance * x_distance + y_distance * y_distance) < (FIGURE_HEIGHT // 2 + BALL_RADIUS):
            if y_distance == 0:
                self.shoot(ball, 3 * math.pi / 2)
            elif y_distance < 0:
                self.shoot(ball, (2 * math.pi - math.atan(x_distance / math.fabs(y_distance))))
            else:
                self.shoot(ball, (math.pi + math.atan(x_distance / math.fabs(y_distance))))
            retval = True
        else:
            retval = False
        return retval

    def shoot(self, ball, new_angle):
        ball.set_new_angle(new_angle)
        ball.set_speed(1000)
        ball.set_new_x_position(ball.get_x_position() + math.sin(ball.get_new_angle()) * ball.get_speed() * self._time)
        ball.set_new_y_position(ball.get_y_position() + math.cos(ball.get_new_angle()) * ball.get_speed() * self._time)


class Strategy(Keeper):
    def __init__(self, speed, time_delta):
        super().__init__(speed, time_delta)

    def new_strategy_step(self, ball):
        if ball.get_angle() > math.pi < 2 * math.pi:
            self._new_desired_pos(self.MAX_POS_KEEPER/2)
        else:
            self._new_desired_pos(ball.get_y_position() - self.OFFSET_VIEW_KEEPER)
