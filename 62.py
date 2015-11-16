# DP solution.
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        trace = [[1] * (n + 1) for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                trace[i][j] = trace[i - 1][j] + trace[i][j - 1]
        return trace[m - 1][n - 1]


