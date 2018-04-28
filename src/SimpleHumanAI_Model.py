import math
import random
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
    POSITION_ON_BAR = 219
    # ABS_X_MIN_POS_KEEPER =

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

        '''if - math.pi / 2 < ball.get_angle() < math.pi / 2:
            x_distance = COURT_WIDTH - X_POSITION_HUMAN_KEEPER + FIGURE_WIDTH / 2 - ball.get_new_x_position()
            y_distance = self._position + self.POSITION_ON_BAR - ball.get_new_y_position()
            abs_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
            if abs_distance < BALL_RADIUS + FIGURE_RADIUS:
                print("Collision", abs_distance)
                interaction = self.ball_gamer_collision(ball)
            elif ball.get_x_position() < COURT_WIDTH - X_POSITION_HUMAN_KEEPER < ball.get_new_x_position():
                interaction = self.check_for_intersection(ball)
            else:
                interaction = False
        else:
            interaction = False
        return interaction'''

        if - math.pi / 2 < ball.get_angle() < math.pi / 2:
            interaction = self.check_for_intersection(ball)
        else:
            interaction = False
        return interaction

    def check_for_intersection(self, ball):
        min_distance_gamer_ball = math.fabs((ball.get_new_x_position() - ball.get_x_position())
                                            * (self._position + self.POSITION_ON_BAR - ball.get_y_position())
                                            - (ball.get_new_y_position() - ball.get_y_position())
                                            * (COURT_WIDTH - X_POSITION_HUMAN_KEEPER + FIGURE_WIDTH / 2
                                               - ball.get_x_position())) / (ball.get_speed() * self._time)
        if min_distance_gamer_ball < BALL_RADIUS + FIGURE_RADIUS:
            interaction = self.check_for_shoot(ball)
        else:
            interaction = False
        return interaction

    def ball_gamer_collision(self, ball):
        return self.check_for_shoot(ball)

    def game_bar_intersection(self, ball):
        y_intersection = (COURT_WIDTH - X_POSITION_HUMAN_KEEPER - ball.get_x_position()) * math.tan(ball.get_angle()) \
                       + ball.get_y_position()
        if math.fabs(self._position + self.POSITION_ON_BAR - y_intersection) < FIGURE_HEIGHT / 2 + BALL_RADIUS\
                or COURT_WIDTH - X_POSITION_HUMAN_KEEPER < \
                ball.get_x_position() < COURT_WIDTH - X_POSITION_HUMAN_KEEPER - FIGURE_WIDTH / 2 - BALL_RADIUS:
            self.check_for_shoot(ball)

    def check_for_shoot(self, ball):
        x_distance = COURT_WIDTH - X_POSITION_HUMAN_KEEPER - ball.get_x_position()
        y_distance = self._position + self.POSITION_ON_BAR - ball.get_y_position()
        abs_distance = math.sqrt(x_distance * x_distance + y_distance * y_distance)
        angle_ball_to_gamer = math.atan2(y_distance, x_distance)
        cross_angle = math.fabs(angle_ball_to_gamer) + ball.get_angle()

        '''if ball.get_angle() > math.pi / 2:
            cross_angle = ball.get_angle() - math.pi / 2 + angle_ball_to_gamer
        else:
            cross_angle = math.pi / 2 - ball.get_angle() - angle_ball_to_gamer'''

        intermediate_result = abs_distance * math.sin(cross_angle) / (BALL_RADIUS + FIGURE_HEIGHT / 2)
        distance_to_collision = math.sqrt((BALL_RADIUS + FIGURE_HEIGHT / 2) * (BALL_RADIUS + FIGURE_HEIGHT / 2)
                                          + abs_distance * abs_distance
                                          - 2 * (BALL_RADIUS + FIGURE_HEIGHT / 2) * abs_distance
                                          * math.cos(intermediate_result))
        print(distance_to_collision)
        if distance_to_collision < ball.get_speed() * self._time:
            self.shoot_2(ball, distance_to_collision)
            interaction = True
        else:
            interaction = False
        return interaction

    def shoot(self, ball, new_angle):
        ball.set_new_angle(new_angle)
        ball.set_speed(2000)
        ball.set_new_x_position(ball.get_x_position() + math.sin(ball.get_new_angle()) * ball.get_speed() * self._time)
        ball.set_new_y_position(ball.get_y_position() + math.cos(ball.get_new_angle()) * ball.get_speed() * self._time)

    def shoot_2(self, ball, distance):
        time_delta_to_collision = distance / ball.get_speed()
        time_delta_after_collision = self._time - time_delta_to_collision
        x_pos_collision = ball.get_x_position() + math.cos(ball.get_angle()
                                                           * ball.get_speed() * time_delta_to_collision)
        y_pos_collision = ball.get_y_position() + math.sin(ball.get_angle()
                                                           * ball.get_speed() * time_delta_to_collision)
        x_distance = COURT_WIDTH - X_POSITION_HUMAN_KEEPER + FIGURE_WIDTH / 2 - x_pos_collision
        y_distance = self._position + self.POSITION_ON_BAR - y_pos_collision
        if int(y_distance) == 0:
            rand_num = random.choice([- 0.01, 0.01])
            if rand_num < 0:
                ball.set_new_angle(math.pi + rand_num)
            else:
                ball.set_new_angle(- math.pi + rand_num)
            ball.set_speed(2000)
            ball.set_new_x_position(
                x_pos_collision + math.cos(ball.get_new_angle()) * ball.get_speed() * time_delta_after_collision)
            ball.set_new_y_position(
                y_pos_collision + math.sin(ball.get_new_angle()) * ball.get_speed() * time_delta_after_collision)
        elif y_distance < 0:
            ball.set_new_angle((math.pi / 2 + math.atan2(x_distance, math.fabs(y_distance))))
            ball.set_speed(2000)
            ball.set_new_x_position(
                x_pos_collision + math.cos(ball.get_new_angle()) * ball.get_speed() * time_delta_after_collision)
            ball.set_new_y_position(
                y_pos_collision + math.sin(ball.get_new_angle()) * ball.get_speed() * time_delta_after_collision)
        else:
            ball.set_new_angle((- math.pi / 2 - math.fabs(math.atan2(x_distance, y_distance))))
            ball.set_speed(2000)
            ball.set_new_x_position(
                x_pos_collision + math.cos(ball.get_new_angle()) * ball.get_speed() * time_delta_after_collision)
            ball.set_new_y_position(
                y_pos_collision + math.sin(ball.get_new_angle()) * ball.get_speed() * time_delta_after_collision)
        print(ball.get_new_angle())
        input()


class Strategy(Keeper):
    def __init__(self, speed, time_delta):
        super().__init__(speed, time_delta)

    def new_strategy_step(self, ball):
        if - math.pi / 2 < ball.get_angle() < math.pi / 2:
            self._new_desired_pos(ball.get_y_position() - self.POSITION_ON_BAR)
        else:
            self._new_desired_pos(self.MAX_POS_KEEPER/2)

