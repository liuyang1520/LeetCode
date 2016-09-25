"""
DP:
dp[i][j] = distinct subsequences of t[:j] in s[:i]
dp[i][0] = 1, for each i, since the only way is to deleting all content;
dp[i][j] = dp[i-1][j-1] + dp[i-1][j], if s[i] == t[j]
dp[i][j] = dp[i-1][j], if s[i] != t[j]
"""
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dp = [[0] * (len(t) + 1) for i in range(len(s) + 1)]
        for i in range(len(dp)):
            dp[i][0] = 1
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]