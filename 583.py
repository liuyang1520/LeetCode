"""
dp[j][j] means the min number of deletion operations as required
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dp = [(len(word2) + 1) * [1000] for i in range(len(word1) + 1)]
        dp[0] = [i for i in range(len(word2) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = min(dp[i][j+1], dp[i+1][j]) + 1
        return dp[-1][-1]
