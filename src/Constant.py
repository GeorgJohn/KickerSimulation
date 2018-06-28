from enum import IntEnum
import math
"""
Datenbank aller Konstanten groeßen der Simulation

Laengenmaße in mm
Geschwindigkeiten in mm/msec
Winkel in rad
Winkelgeschwindigkeit in rad/sec
Farben in RGB
Masse in [g] Gramm
"""

SEC_PER_FRAME = 1 / 60


"""Fenster"""
SCREEN_WIDTH = 1360
SCREEN_HIGH = 840
MARGIN_LEFT = 80
MARGIN_RIGHT = 80
MARGIN_BUTTON = 30
MARGIN_TOP = 130

"""Infofenster"""
INFO_DISP_HIGH = 100

"""Grundfarben"""
WITHE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_BLUE = (11, 36, 158)

"""Spielfeld"""
COURT_WIDTH = 1200
COURT_HEIGHT = 680
GOAL_BAR_POS = 240
GOAL_SIZE = 200
FIELD_COLOUR = (12, 128, 40)
COURT_LINE_THICKNESS = 8
COURT_LINE_POINT_RADIUS = 10
COURT_LINE_CIRCLE_RADIUS = 103

"""Ball"""
BALL_RADIUS = 17
BALL_DIAMETER = 2 * BALL_RADIUS
BALL_MASS = 23.13
BALL_MAX_SPEED = 1000

"""Spielfiguren"""
FIGURE_WIDTH = 10
FIGURE_HEIGHT = 24
SHOOT_SPEED = 1000
FIGURE_RADIUS = round(math.sqrt(FIGURE_WIDTH * FIGURE_WIDTH + (FIGURE_HEIGHT / 2) * (FIGURE_HEIGHT / 2)))
FIGURE_DIAMETER = round(2 * FIGURE_RADIUS)
FIGURE_VIEW_END_ANGLE = math.atan2(FIGURE_HEIGHT / 2, FIGURE_WIDTH)
FIGURE_VIEW_START_ANGLE = 2 * math.pi - FIGURE_VIEW_END_ANGLE

MAX_POS_KEEPER = 242
MAX_POS_DEFENDER = 366
MAX_POS_MIDFIELDER = 114
MAX_POS_FORWARD = 230

X_POSITION_KEEPER = 75


HUMAN_KEEPER_OFFSET_X = MARGIN_LEFT + X_POSITION_KEEPER - FIGURE_WIDTH / 2
HUMAN_KEEPER_OFFSET_Y = (COURT_HEIGHT - MAX_POS_KEEPER) / 2 + MARGIN_TOP - FIGURE_HEIGHT / 2
HUMAN_KEEPER_OFFSET_CIRCLE_X = MARGIN_LEFT + X_POSITION_KEEPER - FIGURE_WIDTH / 2 - FIGURE_RADIUS
HUMAN_KEEPER_OFFSET_CIRCLE_Y = (COURT_HEIGHT - MAX_POS_KEEPER) / 2 + MARGIN_TOP - FIGURE_RADIUS

COMPUTER_KEEPER_OFFSET_X = SCREEN_WIDTH - MARGIN_RIGHT - X_POSITION_KEEPER - FIGURE_WIDTH / 2
COMPUTER_KEEPER_OFFSET_Y = HUMAN_KEEPER_OFFSET_Y


class Coordinate(IntEnum):
    X = 0
    Y = 1
    Z = 2


class Gamer(IntEnum):
    HUMAN = 0
    COMPUTER = 1


class TeamComputer(IntEnum):
    KEEPER = 1
    DEFENDER_RIGHT = 2
    DEFENDER_LEFT = 3
    MIDFIELDER_HALF_RIGHT = 4
    MIDFIELDER_CENTER = 5
    MIDFIELDER_HALF_LEFT = 6
    MIDFIELDER_RIGHT = 7
    FORWARD_RIGHT = 8
    FORWARD_CENTER = 9
    FORWARD_LEFT = 10
    MIDFIELDER_LEFT = 11


class TeamHuman(IntEnum):
    KEEPER = 1
    DEFENDER_RIGHT = 2
    DEFENDER_LEFT = 3
    MIDFIELDER_HALF_RIGHT = 4
    MIDFIELDER_CENTER = 5
    MIDFIELDER_HALF_LEFT = 6
    MIDFIELDER_RIGHT = 7
    FORWARD_RIGHT = 8
    FORWARD_CENTER = 9
    FORWARD_LEFT = 10
    MIDFIELDER_LEFT = 11


class GameBorder(IntEnum):
    TOP = 1
    BUTTON = 2
    LEFT = 3
    RIGHT = 4
