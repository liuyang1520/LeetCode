# DP: dp[i][j] = min(k + max(dp[i][k-1], dp[k+1][j])) for each i < k < j
# dp[i][j] meas the min cost to guarantee a win within [i, j]
# For example, when n = 3:
# first calculate dp[1][2] = 1, dp[2][3] = 2
# then dp[1][3] = min(1 + max(d[1][2], dp[2][3]), 2 + max(0, 0)) = 2
class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                dp[j-i][j] = min([k + max(dp[j-i][k-1], dp[k+1][j]) for k in range(j-i, j)])
        return dp[1][n]