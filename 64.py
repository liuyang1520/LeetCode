# Simple DP problem.
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif i > 0 and j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                elif i > 0 and j > 0:
                    grid[i][j] = min(grid[i - 1][j] + grid[i][j], grid[i][j - 1] + grid[i][j])
        return grid[-1][-1]