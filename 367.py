# Newton's method
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
