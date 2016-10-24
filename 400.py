"""
1-9     9 nums
10-99   90 nums
100-999 900 nums
...
"""
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        digits = 1
        test = n
        while test > (10**(digits-1)) * 9 * digits:
            test -= (10**(digits-1)) * 9 * digits
            digits += 1
        num, rem = int(math.ceil(test*1.0 / digits)) + 10**(digits-1) - 1, test % digits
        return int(str(num)[rem - 1])