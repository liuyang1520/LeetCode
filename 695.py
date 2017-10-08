"""
DFS
"""
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.xmax, self.ymax = len(grid), len(grid[0])
        maxArea = 0
        self.grid = grid
        self.subArea = 0
        for i in range(self.xmax):
            for j in range(self.ymax):
                if not grid[i][j]:
                    continue
                else:
                    self.getArea(i, j)
                    maxArea = max(maxArea, self.subArea)
                    self.subArea = 0
        return maxArea

    def getArea(self, x, y):
        self.grid[x][y] = 0
        self.subArea += 1
        for x_offset, y_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_new, y_new = x+x_offset, y+y_offset
            if 0 <= x_new < self.xmax and 0 <= y_new < self.ymax and self.grid[x_new][y_new]:
                self.grid[x_new][y_new] = 0
                self.getArea(x_new, y_new)
