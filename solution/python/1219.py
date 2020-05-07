"""
@difficulty: medium
@tags: DFS
@notes: For each cell, we perform a DFS to get the largest path.
In order to run the DFS without calculating duplicate cells, we have at least 3 ways:
- deep copy the current state of grid, and pass into next recursion, every recursion has its own state of grid
- update the original grid to remove gold, and add it back in the same recursion after calling dfs
- use a set to track the visited cells, add it in the beginning of this recursion and remove it after calling dfs
For simplicity, we use the first way, and it is easier to track the actual path if we need.
"""
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.xmax = len(grid)
        self.ymax = len(grid[0])
        self.grid = grid
        self.totalMax = 0
        for i in range(self.xmax):
            for j in range(self.ymax):
                gridCopy = [grid[k][:] for k in range(self.xmax)]
                self.dfs(gridCopy, i, j, 0)
        return self.totalMax

    def dfs(self, grid, x, y, total):
        if not grid[x][y]:
            return
        total += grid[x][y]
        grid[x][y] = 0
        if total > self.totalMax:
            self.totalMax = total
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xn, yn = x + dx, y + dy
            if 0 <= xn < self.xmax and 0 <= yn < self.ymax and grid[xn][yn]:
                gridCopy = [grid[k][:] for k in range(self.xmax)]
                self.dfs(gridCopy, xn, yn, total)
