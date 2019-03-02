"""
sqrt is the optimal solution
"""
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        mid = int(area ** 0.5)
        for i in range(mid, 0, -1):
            if area % i == 0:
                return [area / i, i]