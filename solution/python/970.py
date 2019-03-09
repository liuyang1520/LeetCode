"""
@difficulty: easy
@tags: misc
@notes: Brute-Force with log function to save time.
"""
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        import math
        res = set()
        if bound == 0: return []
        xMax, yMax = 0 if x == 1 else int(math.log(bound, x)), 0 if y == 1 else int(math.log(bound, y))
        for i in range(xMax+1):
            for j in range(yMax+1):
                subsum = x ** i + y ** j
                if subsum <= bound:
                    res.add(subsum)
        return list(res)
