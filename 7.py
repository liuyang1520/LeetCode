# Pythonic way solution
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = x / abs(x) if x != 0 else 0
        x = abs(x)
        ans = int(str(x)[::-1])
        if ans > 2147483647:
            return 0
        return flag * ans