"""
2D DP
"""
class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [[float('inf')] * (len(s2) + 1) for i in range(len(s1) + 1)]
        dp[0][0] = 0
        for i in range(1, len(dp)):
            dp[i][0] = ord(s1[i-1]) + dp[i-1][0]
        for i in range(1, len(dp[0])):
            dp[0][i] = ord(s2[i-1]) + dp[0][i-1]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))
        return dp[-1][-1]
