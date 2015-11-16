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


# Math solution. f(m, n) = C_(m+n-2)^(m-1).
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > n:
            m, n = n, m
        if m == 1 or n == 1:
            return 1
        res = reduce(lambda x, y: x * y, [i for i in range(n, m + n - 2 + 1)])
        div = reduce(lambda x, y: x * y, [i for i in range(1, m)])
        return res / div