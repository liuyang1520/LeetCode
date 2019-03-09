"""
2D DP, dp[i][j] is the max length from i to j, inclusive.
Solution 1, TLE, no need to write another loop inside
Solution 2, need if s == s[::-1]: return len(s), otherwise TLE
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        # init 2D dp
        dp = [[0]*length for i in range(length)]
        # base values
        for i in range(length):
            dp[i][i] = 1
        # update dp
        for delta in range(1, length):
            for i in range(length - delta):
                j = i + delta
                for k in range(i, j):
                    if s[j] == s[k]:
                        dp[i][j] = max(dp[i][j], dp[k+1][j-1] + 2)
                    else:
                        dp[i][j] = max(dp[i][j-1], dp[i][j])
        return dp[0][-1]

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == s[::-1]: return len(s)
        length = len(s)
        # init 2D dp
        dp = [[0]*length for i in range(length)]
        # base values
        for i in range(length):
            dp[i][i] = 1
        # update dp
        for delta in range(1, length):
            for i in range(length - delta):
                j = i + delta
                dp[i][j] = max(dp[i][j-1], dp[i+1][j])
                if s[j] == s[i]:
                    dp[i][j] = dp[i+1][j-1] + 2
        return dp[0][-1]
