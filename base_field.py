"""
This module sets the base behaviour of all playing fields.
"""


class BaseField:

    def __init__(self, field_size):
        """

        :param field_size: integer, field_size>=5.
        """
        self.field = [[0] * field_size for i in range(field_size)]
        self.size = field_size
        self.row_length = 5

    def check_row_impropriety(self, point, direction):
        def check_axis_impropriety(coordinate):
            return point[coordinate] + (self.row_length - 1) * direction[coordinate] >= self.size or \
                   point[coordinate] + (self.row_length - 1) * direction[coordinate] < 0 or \
                   point[coordinate] >= self.size or \
                   point[coordinate] < 0
        return check_axis_impropriety(0) or check_axis_impropriety(1)

    def clear(self):
        """

        This function sets the playing field empty.
        :return:
        """
        for i in range(self.size):
            for j in range(self.size):
                self.field[i][j] = 0
