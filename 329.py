"""
Sol 1: DFS + DP[x][y]
Sol 2: sorted list + DP[x][y]
    1) pull values from matrix into a list [(x, y, val), ...], x,y are position, val is the value;
    2) sort the list according to val;
    3) update dp[x][y] iteratively starting from the lowest val.
""" 
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        x_len = len(matrix)
        y_len = len(matrix[0])
        dp = [[1] * y_len for i in range(x_len)]
        
        sortedList = sorted([(i, j, val)
                for i, row in enumerate(matrix)
                for j, val in enumerate(row)
            ], key = lambda x: x[2])
            
        for x, y, val in sortedList:
            for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                x_new, y_new = x + dx, y + dy
                if 0 <= x_new < x_len and 0 <= y_new < y_len and matrix[x_new][y_new] > val:
                    dp[x_new][y_new] = max(dp[x][y] + 1, dp[x_new][y_new])
        return max([max(row) for row in dp])
        