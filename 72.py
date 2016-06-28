# DP problem.
# See http://www.cnblogs.com/springfor/p/3896167.html
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [[float('Inf') for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for s in range(len(dp)):
            dp[s][0] = s
        for s in range(len(dp[0])):
            dp[0][s] = s
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]
