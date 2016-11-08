"""
Math, f(1) = 10, ..., f(k) = 9 * 9 * 8 * ... (9 - k + 2)
"""
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        def getCount(k):
            if k == 1:
                return 9
            res, i = 9, 2
            while i <= k:
                res *= 9 - i + 2
                i += 1
            return res
        
        res = 1
        for i in range(1, n+1):
            res += getCount(i)
        return res