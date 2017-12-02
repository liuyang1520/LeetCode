"""
DP solution, the largest divider would be the optimal
"""
class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = (n+1) * [float('inf')]
        dp[0] = dp[1] = 0
        for i in range(1, n+1):
            for j in range(i-1, 0, -1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i / j)
                    break
        return dp[n]
