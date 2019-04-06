"""
This module sets the behaviour of the playing field which interacts with the user.
"""
from game_states import GAME_STATE
from base_field import BaseField


class Field(BaseField):

    def field_print(self):
        """

        This function prints the playing field.
        :return:
        """
        code_list = ['.', 'X', 'O']
        out_str = '  '
        for i in range(self.size):
            out_str = out_str + (i < 9) * ' ' + ' ' + str(i + 1)
        print(out_str)
        for i in range(self.size):
            out_str = (i < 9) * ' ' + str(i + 1)
            for j in range(self.size):
                out_str = out_str + '  ' + code_list[self.field[i][j]]
            print(out_str)

    def put_x(self, x, y):
        """

        This function puts "X" to (x,y) coordinates.
        :param x: integer, 1 <= x <= field_size.
        :param y: integer, 1 <= y <= field_size.
        :return:
        """
        self.field[y - 1][x - 1] = 1

    def put_o(self, x, y):
        """

        This function puts "O" to (x,y) coordinates.
        :param x: integer, 1 <= x <= field_size.
        :param y: integer, 1 <= y <= field_size.
        :return:
        """
        self.field[y - 1][x - 1] = 2

    def get(self, x, y):
        """

        This functions returns the type of the cell.
        :param x: integer, 1 <= x <= field_size.
        :param y: integer, 1 <= y <= field_size.
        :return: 0 if cell is empty, 1 if there is "X", 2 if there is "O".
        """
        return self.field[y - 1][x - 1]

    def check(self):
        """

        This function checks the end of the game.
        :return: GameState.not_ended if the game hasn't been ended yet, GameState.win_first if "X" have won,
                 GameState.win_second if "O" have won, GameState.draw if it is the draw.
        """
        is_draw = True
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 0:
                    is_draw = False
        if is_draw:
            return GAME_STATE.draw
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 0:
                    continue
                # List of the investigated directions.
                directions = [(1, 1), (0, 1), (1, 0), (-1, 1)]
                for direction in directions:
                    if self.check_row_impropriety((i, j), direction):
                        continue
                    fl = True
                    for k in range(1, self.row_length):
                        if self.field[i + k * direction[0]][j + k * direction[1]] != \
                           self.field[i][j]:
                            fl = False
                    if fl:
                        if self.field[i][j] == 1:
                            return GAME_STATE.win_first
                        if self.field[i][j] == 2:
                            return GAME_STATE.win_second
        return GAME_STATE.not_ended
