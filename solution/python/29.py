"""
1. use division
2. a / b = a - b - b - b ....
	but it is too slow, so,
	a / b = a - b - 2b - 4b ...
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31-1
        return min(MAX_INT, int(float(dividend) / divisor))


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 2**31-1
        x, y = abs(dividend), abs(divisor)
        if x < y:
            return 0
        base, count, res = 0, 0, 0
        while x >= y:
            base, count = y, 1
            while base + base <= x:
                base += base
                count += count
            x -= base
            res += count
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            return 0 - res
        else:
            return min(res, MAX_INT)