# Division solution.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n / 2 != 0:
            if n % 2 == 1:
                res += 1
            n = n / 2
        if n == 1:
            res += 1
        return res


# Python solution.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count("1")


# Bit operation solution.
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            res += n & 1
            n >>= 1
        return res