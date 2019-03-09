"""
Recusion + memorize
"""
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        stats = {0: 0, 1: 1}
        def helper(n):
            if n in stats:
                return stats[n]
            res = helper(n-1) + helper(n-2)
            stats[n] = res
            return res

        return helper(N)
