from enum import Enum

class GameState(Enum):

    not_ended = 0
    win_first = 1
    win_second = 2
    draw = 3