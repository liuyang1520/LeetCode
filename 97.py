"""
2D-DP
dp[i][j] means whether s1[0:i+1] and s2[0:j+1] interleave s3[0:i+j+1]
dp[i][j] = (dp[i-1][j] == 1 and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] == 1 and s2[j-1] == s3[i+j-1])
"""
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1, l2, l3 = len(s1), len(s2), len(s3)
        dp = [[0] * (l2+1) for i in range(l1+1)]
        if l1 + l2 != l3:
            return False
        dp[0][0] = 1
        for i in range(l1 + 1):
            for j in range(l2 + 1):
                if i == 0 and j > 0:
                    dp[i][j] = 1 if (dp[i][j-1] == 1 and s2[j-1] == s3[j-1]) else 0
                elif j == 0 and i > 0:
                    dp[i][j] = 1 if (dp[i-1][j] == 1 and s1[i-1] == s3[i-1]) else 0
                elif i > 0 and j > 0:
                    dp[i][j] = 1 if (dp[i-1][j] == 1 and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] == 1 and s2[j-1] == s3[i+j-1]) else 0
        return bool(dp[l1][l2])