import math
import random
from src.Constant import*


class GameBar:
    """Konstanten"""
    SHOOT_SPEED = 2000

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
    POSITION_ON_BAR = 219
    ABS_X_POSITION = COURT_WIDTH - X_POSITION_KEEPER
    X_REFLECTION_PLANE = COURT_WIDTH - X_POSITION_KEEPER - FIGURE_WIDTH / 2 - BALL_RADIUS
    X_OFFSET_REFLECTION_PLANE = FIGURE_WIDTH / 2 + BALL_RADIUS
    Y_OFFSET_REFLECTION_PLANE = FIGURE_HEIGHT / 2 + BALL_RADIUS

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

    def check_for_interaction(self, ball):

        if ball.get_x_position() < self.X_REFLECTION_PLANE:
            if self.X_REFLECTION_PLANE - ball.get_x_position() <= ball.get_new_x_position() - ball.get_x_position():
                interaction = self.check_for_shoot(ball)
            else:
                interaction = False
        elif ball.get_x_position() - self.X_REFLECTION_PLANE < (ball.get_speed() * self._time
                                                                + 2 * self.X_OFFSET_REFLECTION_PLANE):
            interaction = self.check_for_side_collision(ball)
        else:
            interaction = False
        return interaction

    def check_for_shoot(self, ball):
        intersection = ball.get_y_position() + math.tan(ball.get_angle())\
                       * (self.X_REFLECTION_PLANE - ball.get_x_position())
        if self._position + self.POSITION_ON_BAR - self.Y_OFFSET_REFLECTION_PLANE < intersection \
                < self._position + self.POSITION_ON_BAR + self.Y_OFFSET_REFLECTION_PLANE:
            self.shoot(ball, intersection)
            interaction = True
        else:
            interaction = False
        return interaction

    def shoot(self, ball, intersection):
        delta_t_collision = (self.X_REFLECTION_PLANE - ball.get_x_position()) / \
                            (math.cos(ball.get_angle()) * ball.get_speed())
        shoot_offset = self._position + self.POSITION_ON_BAR - intersection
        if shoot_offset < 0:
            ball.set_new_angle(math.pi + shoot_offset / (FIGURE_HEIGHT + BALL_DIAMETER))
        elif shoot_offset > 0:
            ball.set_new_angle(- math.pi + shoot_offset / (FIGURE_HEIGHT + BALL_DIAMETER))
        else:
            ball.set_new_angle(math.pi)
        ball.set_speed(self.SHOOT_SPEED)
        ball.set_new_y_position(ball.get_y_position() +
                                math.sin(ball.get_angle()) * ball.get_speed() * self._time)
        ball.set_new_x_position(self.X_REFLECTION_PLANE +
                                math.cos(ball.get_new_angle()) *
                                ball.get_speed() * (self._time - delta_t_collision))

    def check_for_side_collision(self, ball):
        if ball.get_y_position() < self._position + self.POSITION_ON_BAR - self.Y_OFFSET_REFLECTION_PLANE \
                and ball.get_angle() > 0:
            if ball.get_new_y_position() > self._position + self.POSITION_ON_BAR - self.Y_OFFSET_REFLECTION_PLANE:
                intersection = ball.get_x_position()\
                               + (self._position + self.POSITION_ON_BAR - self.Y_OFFSET_REFLECTION_PLANE
                                  - ball.get_y_position()) / math.tan(ball.get_angle())
                if self.ABS_X_POSITION - self.X_OFFSET_REFLECTION_PLANE < intersection \
                        < self.ABS_X_POSITION + self.X_OFFSET_REFLECTION_PLANE:
                    delta_t_collision = (self._position + self.POSITION_ON_BAR - self.Y_OFFSET_REFLECTION_PLANE
                                         - ball.get_y_position()) / (math.sin(ball.get_angle()) * ball.get_speed())
                    ball.set_new_angle(- ball.get_angle())
                    ball.set_new_x_position(ball.get_x_position() +
                                            math.cos(ball.get_angle()) * ball.get_speed() * self._time)
                    ball.set_new_y_position(self._position + self.POSITION_ON_BAR - self.Y_OFFSET_REFLECTION_PLANE
                                            + math.sin(ball.get_new_angle())
                                            * ball.get_speed() * (self._time - delta_t_collision))
                    interaction = True
                else:
                    interaction = False
            else:
                interaction = False
        elif ball.get_y_position() > self._position + self.POSITION_ON_BAR + self.Y_OFFSET_REFLECTION_PLANE \
                and ball.get_angle() < 0:
            if ball.get_new_y_position() < self._position + self.POSITION_ON_BAR + self.Y_OFFSET_REFLECTION_PLANE:
                intersection = ball.get_x_position() \
                               + (ball.get_y_position() - self._position - self.POSITION_ON_BAR
                                  - self.Y_OFFSET_REFLECTION_PLANE) / math.tan(ball.get_angle())
                if self.ABS_X_POSITION - self.X_OFFSET_REFLECTION_PLANE < intersection \
                        < self.ABS_X_POSITION + self.X_OFFSET_REFLECTION_PLANE:
                    delta_t_collision = (ball.get_y_position() - self._position - self.POSITION_ON_BAR
                                         - self.Y_OFFSET_REFLECTION_PLANE)\
                                        / (math.sin(ball.get_angle()) * ball.get_speed())
                    ball.set_new_angle(- ball.get_angle())
                    ball.set_new_x_position(ball.get_x_position() +
                                            math.cos(ball.get_angle()) * ball.get_speed() * self._time)
                    ball.set_new_y_position(self._position + self.POSITION_ON_BAR + self.Y_OFFSET_REFLECTION_PLANE
                                            + math.sin(ball.get_new_angle())
                                            * ball.get_speed() * (self._time - delta_t_collision))
                    interaction = True
                else:
                    interaction = False
            else:
                interaction = False
        else:
            interaction = False
        if interaction:
            print(interaction)
        return interaction


class Strategy(Keeper):
    def __init__(self, speed, time_delta):
        super().__init__(speed, time_delta)

    def new_strategy_step(self, ball):
        if - math.pi / 2 < ball.get_angle() < math.pi / 2:
            self._new_desired_pos(ball.get_y_position() - self.POSITION_ON_BAR)
        else:
            self._new_desired_pos(self.MAX_POS_KEEPER/2)

