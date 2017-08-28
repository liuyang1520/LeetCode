"""
Only need to test whether the last point is the origin point
"""
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        visited = set([(x, y)])
        moveOffsets = {"U": [0, 1], "D": [0, -1], "L": [-1, 0], "R": [1, 0]}
        for i in moves:
            x += moveOffsets[i][0]
            y += moveOffsets[i][1]
        if (x, y) == (0, 0):
            return True
        return False
