# Solution 1: Newton's method
# Solution 2: binary search
# Solution 3: any square number = 1 + 3 + 5 + 7 + ... + 2*n + 1, since n^2 - (n-1)^2 = 2n - 1, then do the summation
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x0 = float(num)
        x_new = x0 / 2.0 + num / 2.0 / x0
        while x0 - x_new > 0.00001:
            x0 = x_new
            x_new = x0 / 2.0 + num / 2.0 / x0
        if abs(int(x_new) - x_new) < 0.00001:
            return True
        else:
            return False
