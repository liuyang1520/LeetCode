"""
@difficulty: easy
@tags: math
@notes: Max is alwasy c - a - 2, Min will be 0, 1, 2 only.
"""
class Solution(object):
    def numMovesStones(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        a, b, c = sorted([a, b, c])
        if c - a == 2:
            return [0, 0]
        if b - a <= 2 or c - b <= 2:
            return [1, c - a - 2]
        return [2, c - a - 2]
