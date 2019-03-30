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


# Setting the interaction with user.
print("We are starting a new game.")
game_field.field_print()
state = 1
while True:
    input_cmd = input().split()
    # If we are gaming.
    if state == 1:
        if (input_cmd[0] == "move") and (len(input_cmd) == 3) and input_cmd[1].isdigit() and input_cmd[2].isdigit():
            if (1 <= int(input_cmd[1]) <= field_size) and (1 <= int(input_cmd[2]) <= field_size):
                if game_field.get(int(input_cmd[1]), int(input_cmd[2])) == 0:
                    game_field.put_x(int(input_cmd[1]), int(input_cmd[2]))
                    x1, y1 = second_player.put(int(input_cmd[1]), int(input_cmd[2]))
                    print("Computer move: {} {}.".format(x1, y1))
                    game_field.put_o(x1, y1)
                    game_field.field_print()
                    winner = game_field.check()
                    if winner == GameState.not_ended:
                        state = 1
                        continue
                    elif winner == GameState.win_first:
                        print("You win.")
                    elif winner == GameState.win_second:
                        print("Computer win.")
                    elif winner == GameState.draw:
                        print("Draw.")
                    print("Start another game?(Y/N)")
                    state = 2
                else:
                    print("Occupied cell. Repeat the command.")
                    state = 1
            else:
                print("Wrong cell. Repeat the command.")
                state = 1
        elif input_cmd == ["exit"]:
            print("Start another game?(Y/N)")
            state = 2
        else:
            print("Wrong input. Repeat the command.")
            state = 1
    # If the game is ended.
    elif state == 2:
        if input_cmd == ["Y"]:
            game_field.clear()
            second_player.clear()
            print("We are starting a new game.")
            game_field.field_print()
            state = 1
        elif input_cmd == ["N"]:
            sys.exit(0)
        else:
            print("Wrong input. Start another game?(Y/N)")
            state = 2
    else:
        print("This is very strange. Game ends.")
        sys.exit(0)
