class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        xMax, yMax = len(grid), len(grid[0])
        count = 0
        for i in range(xMax):
            for j in range(yMax):
                if grid[i][j] > 0:
                    count += 2
                if j == 0:
                    count += grid[i][j]
                else:
                    count += abs(grid[i][j] - grid[i][j-1])
            count += grid[i][-1]
        for j in range(yMax):
            for i in range(xMax):
                if i == 0:
                    count += grid[i][j]
                else:
                    count += abs(grid[i][j] - grid[i-1][j])
            count += grid[-1][j]
        return count
