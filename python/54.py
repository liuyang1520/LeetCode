# The edge cases are troubles for this problem.
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        total = len(matrix) * len(matrix[0])
        x, y, direction = 0, 0, "right"
        x_max, x_min, y_max, y_min = len(matrix[0]), 0, len(matrix), 0
        if x_max == 1:
            return [i[0] for i in matrix]
        if y_max == 1:
            return matrix[0]
        while total:
            res.append(matrix[y][x])
            if direction == "right" and x + 1 < x_max:
                x += 1
            elif direction == "right" and x + 1 == x_max:
                y += 1
                y_min += 1
                direction = "down"
            elif direction == "down" and y + 1 < y_max:
                y += 1
            elif direction == "down" and y + 1 == y_max:
                x -= 1
                x_max -= 1
                direction = "left"
            elif direction == "left" and x > x_min:
                x -= 1
            elif direction == "left" and x == x_min:
                y -= 1
                y_max -= 1
                direction = "up"
            elif direction == "up" and y > y_min:
                y -= 1
            elif direction == "up" and y == y_min:
                x += 1
                x_min += 1
                direction = "right"
            total -= 1
        return res