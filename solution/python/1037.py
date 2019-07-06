"""
@difficulty: easy
@tags: math
@note: Edge cases, duplicate points, slope is inf.
"""
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        if len(set(map(tuple, points))) != len(points):
            return False
        if (points[0][1] - points[1][1]) == 0 and (points[1][1] - points[2][1]) == 0:
            return False
        elif (points[0][1] - points[1][1]) != 0 and (points[1][1] - points[2][1]) != 0:
            return float(points[0][0] - points[1][0]) / (points[0][1] - points[1][1]) != float(points[1][0] - points[2][0]) / (points[1][1] - points[2][1])
        return True
