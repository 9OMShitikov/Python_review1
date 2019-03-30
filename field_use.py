"""
This module sets the behaviour of the playing field.
"""
from game_states import GameState


class Field:

    def __init__(self, field_size):
        """

        :param field_size: integer, field_size>=5.
        """
        self.field = [[0] * field_size for i in range(field_size)]
        self.size = field_size
        self.row_length = 5

    def field_print(self):
        """

        This function prints the playing field.
        :return:
        """
        code_list = ['.', 'X', 'O']
        out_str = '  '
        for i in range(self.size):
            out_str = out_str + (i < 10)*' ' + ' ' + str(i + 1)
        print(out_str)
        for i in range(self.size):
            out_str = (i < 9)*' ' + str(i + 1)
            for j in range(self.size):
                out_str = out_str + '  ' + code_list[self.field[i][j]]
            print(out_str)

    def clear(self):
        """

        This function sets the playing field empty.
        :return:
        """
        for i in range(self.size):
            for j in range(self.size):
                self.field[i][j] = 0

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
        :return: 0 if the game hasn't been ended yet, 1 if "X" have won, 2 if "O" have won, 3 if it is the draw.
        """
        is_draw = True
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 0:
                    is_draw = False
        if is_draw:
            return GameState.draw
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 0:
                    continue
                # List of the investigated directions.
                vector_list = [(1, 1), (0, 1), (1, 0)]
                for direction in range(len(vector_list)):
                    if i + (self.row_length - 1) * vector_list[direction][0] >= self.size or \
                       j + (self.row_length - 1) * vector_list[direction][1] >= self.size:
                        continue
                    fl = True
                    for k in range(1, self.row_length):
                        if self.field[i + k * vector_list[direction][0]][j + k * vector_list[direction][1]] != \
                           self.field[i][j]:
                            fl = False
                    if fl:
                        if self.field[i][j] == 1:
                            return GameState.win_first
                        if self.field[i][j] == 2:
                            return GameState.win_second
        return GameState.not_ended
