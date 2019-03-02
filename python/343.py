# 6 = 3 + 3, 7 = 3 + 2 + 2... It is not hard to find that using 3 is the best choice. So try to use as much 3 as possible,
# if 4 left, then use 2 * 2 = 4, otherwise using 2 instead.
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return int(pow(3, n / 3))
        elif n % 3 == 2:
            return int(pow(3, n / 3)) * 2
        else:
            return int(pow(3, (n - 4) / 3)) * 4