"""
@difficulty: medium
@tags: DP
@notes: dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + int(text1[i-1] == text2[j-1]))
"""
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        len1, len2 = len(text1), len(text2)
        dp = [[0] * (len2 + 1) for i in range(len1 + 1)]
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + int(text1[i-1] == text2[j-1]))
        return dp[-1][-1]
