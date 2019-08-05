"""
@difficulty: easy
@tags: math, dp
@notes: DP or just return N % 2 == 0.
"""
class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        dp = [False] * (N + 1)
        for i in range(2, N + 1):
            for j in range(1, i):
                if i % j == 0 and not dp[i-j]:
                    dp[i] = True
                    break
        return dp[N]
