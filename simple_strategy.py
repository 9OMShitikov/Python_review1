"""
This module sets the behaviour of opponent.
"""
from base_field import BaseField


class Player(BaseField):

    def put(self, x, y):
        """

        This function puts the "O" to the opponent's playing field and returns opponent's answer.
        :param x: integer, 1 <= x <= field_size.
        :param y: integer, 1 <= y <= field_size.
        :return:
        """
        self.field[y - 1][x - 1] = 1
        ans = (-1, -1)
        max_rate = -1
#       Finding the move with the highest rating.
        for i in range(self.size):
            for j in range(self.size):
                if self.field[i][j] == 0:
                    new_rate = self.rate(i, j)
                    if new_rate > max_rate or ans == (-1, -1):
                        ans = (j + 1, i + 1)
                        max_rate = new_rate
        self.field[ans[1] - 1][ans[0] - 1] = 2
        return ans

    def rate(self, p, q):
        """

        This function is rating the move.
        :param p: y - coordinate of the pondered move cell. Integer, 0 <= p <= field_size-1.
        :param q: x - coordinate of the pondered move cell. Integer, 0 <= q <= field_size-1.
        :return:
        """
        cost_x = 0
        cost_o = 0
#       Costs of the underfilled lines with the 1, 2, 3, 4, 5, - length
        costs = {0: 0, 1: 10, 2: 50, 3: 5000, 4: 10000000, 5: 0}
#       List of the directions we're looking.
        directions_list = [(1, 1), (1, 0), (0, 1), (-1, 1)]
        for direction in directions_list:
            for j in range(-4, 1):
                if not self.check_row_impropriety((p + j*direction[0], q + j*direction[1]), direction):
                    # Counts of empty, "X" and "O" cells on the segment.
                    cells_count = [0, 0, 0]
                    for k in range(5):
                        cells_count[self.field[p + (j + k)*direction[0]][q + (j + k)*direction[1]]] += 1
                    if cells_count[2] == 0:
                        cost_x += costs[cells_count[1]]
                    if cells_count[1] == 0:
                        cost_o += costs[cells_count[2]]
        return cost_x + cost_o + cost_x // 10
