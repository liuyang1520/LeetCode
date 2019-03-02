"""
Two method:
1. convert number to string and test whether 00 or 11 in it
2. fetch the right most digit one by one
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        isOne = None
        while n:
            if isOne == bool(n & 1):
                return False
            else:
                isOne = bool(n & 1)
                n >>= 1
        return True
