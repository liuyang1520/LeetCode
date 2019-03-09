# Pythonic solution
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return int(x**0.5)


"""
Binary search, from 0 - x/2 + 1, since:
(x/2 + 1)^2 = x^2/4 + 1 + x >= x, when x >= 0
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start, end = 0, x/2 + 1
        while start <= end:
            mid = (start + end) / 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1


"""
Newton's method, https://en.wikipedia.org/wiki/Newton%27s_method
The classical way of calculating the roots.
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        root = x / 2 + 1
        while root ** 2 > x:
            root = int(root/2.0 + x/(2.0 * root))
        return root