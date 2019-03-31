import sys
from enum import Enum
import field_use
import simple_strategy
from game_states import GameState


class SessionState(Enum):

    game = 0
    end_of_game = 1


field_size = 15
game_field = field_use.Field(field_size)
second_player = simple_strategy.Player(field_size)


# Checking the validity of the move.
def check_wrong_move(given_cmd):
    """

    This function checks the impropriety of the move.
    :param given_cmd: list of three positions. Last two are the integer x- and y-coordinates of the move.
    :return: true if the move is wrong, false if it isn't.
    """
    if 1 > int(given_cmd[1]) or field_size < int(given_cmd[1]) or \
            1 > int(given_cmd[2]) or field_size < int(given_cmd[2]):
        print("Wrong cell. Repeat the command.")
        return True
    if game_field.get(int(given_cmd[1]), int(given_cmd[2])) != 0:
        print("Occupied cell. Repeat the command.")
        return True


# Answering to the move command.
def interact_move(given_cmd):
    """

    This function gives the move to the game and the opponent and checks the reactions of them.
    :param given_cmd: list of three positions. Last two are the integer x- and y-coordinates of the move.
    :return: the GameState state of the game.
    """
    game_field.put_x(int(given_cmd[1]), int(given_cmd[2]))
    x1, y1 = second_player.put(int(given_cmd[1]), int(given_cmd[2]))
    print("Computer move: {} {}.".format(x1, y1))
    game_field.put_o(x1, y1)
    game_field.field_print()
    winner = game_field.check()
    if winner == GameState.not_ended:
        return SessionState.game
    elif winner == GameState.win_first:
        print("You win.")
    elif winner == GameState.win_second:
        print("Computer win.")
    elif winner == GameState.draw:
        print("Draw.")
    print("Start another game?(Y/N)")
    return SessionState.end_of_game


# Setting the interaction with user.
print("We are starting a new game.")
game_field.field_print()
state = SessionState.game
while True:
    input_cmd = input().split()
    # If we are gaming.
    if state == SessionState.game:
        if input_cmd[0] == "move" and len(input_cmd) == 3 and input_cmd[1].isdigit() and input_cmd[2].isdigit():
            if check_wrong_move(input_cmd):
                continue
            state = interact_move(input_cmd)
        elif input_cmd == ["exit"]:
            print("Start another game?(Y/N)")
            state = SessionState.end_of_game
        else:
            print("Wrong input. Repeat the command.")
            state = SessionState.game

    # If the game is ended.
    elif state == SessionState.end_of_game:
        if input_cmd == ["Y"]:
            game_field.clear()
            second_player.clear()
            print("We are starting a new game.")
            game_field.field_print()
            state = SessionState.game
        elif input_cmd == ["N"]:
            sys.exit(0)
        else:
            print("Wrong input. Start another game?(Y/N)")
            state = SessionState.end_of_game
    else:
        print("This is very strange. Game ends.")
        sys.exit(0)
