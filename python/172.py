# number of zeros = n / 5 + n / 25 + n / 125 + ...
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeros = 0
        div = 5
        while n >= div:
            zeros += n / div
            div *= 5
        return zeros