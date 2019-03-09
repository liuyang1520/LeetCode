"""
(1+k)*k / 2 <= n
k <= sqrt(2*n + 1/4) - 1/2
"""
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((2*n+1.0/4)**0.5-0.5)