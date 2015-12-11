# DP problem.
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 0:
                    if i == 0 and j > 0:
                            dp[i][j] = dp[i][j - 1]
                    elif j == 0 and i > 0:
                            dp[i][j] = dp[i - 1][j]
                    elif j > 0 and i > 0:
                            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]