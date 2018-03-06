class GameBar:
    def __init__(self, position: float, acceleration: float, max_speed: float, time_delta: float):
        self._position = position
        self._next_position = -1
        self._speed = 0
        self._acceleration = acceleration
        self._max_speed = max_speed
        self._time_delta = time_delta

    def get_position(self):
        return self._position

    def get_next_pos(self):
        return self._next_position

    def set_next_pos(self, next_pos):
        self._next_position = next_pos

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

    def __init__(self, max_speed, time_delta):
        super().__init__(self.MAX_POS_KEEPER / 2, 0, max_speed, time_delta)

    def move_to_position(self, next_pos):
        retval = False
        if next_pos <= self.MAX_POS_KEEPER >= 0:
            self._next_position = next_pos
            if round(self._next_position) == round(self._position):
                self.stop()
                self._next_position = -1
            elif self._next_position < self._position:
                self.move_up()
            else:
                self.move_down()
        else:
            retval = False

        return retval

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

    def stop(self):
        self.set_speed(0)
        self.set_next_pos(-1)


'''
class ComputerAI_Gamer:
    def __init__(self):
        self.__pos_keeper = Const.MAX_POS_KEEPER / 2
        self.__pos_defender = Const.MAX_POS_DEFENDER / 2
        self.__pos_midfielder = Const.MAX_POS_MIDFIELDER / 2
        self.__pos_forward = Const.MAX_POS_FORWARD / 2
        self.__acceleration_keeper = 0
        self.__acceleration_defender = 0
        self.__acceleration_midfielder = 0
        self.__acceleration_forward = 0

    def move(self):
        """Hier die neue Spielerposition ausrechnen"""

    def get_keeper_pos(self):
        return self.__pos_keeper
'''