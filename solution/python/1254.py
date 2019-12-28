"""
@difficulty: medium
@tags: DFS
@notes: Convert 4 edges to water, then count the remaining islands.
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        xmax, ymax = len(grid), len(grid[0])
        def dfsCovertToWater(x, y):
            if grid[x][y]:
                return
            grid[x][y] = 1
            shift = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in shift:
                xn, yn = x + dx, y + dy
                if xn < 0 or xn == xmax or yn < 0 or yn == ymax or grid[xn][yn]:
                    continue
                dfsCovertToWater(xn, yn)
        # Convert 4 edges to water
        for i in [0, xmax-1]:
            for j in range(ymax):
                dfsCovertToWater(i, j)
        for j in [0, ymax-1]:
            for i in range(xmax):
                dfsCovertToWater(i, j)
        # Count the remaining islands
        count = 0
        for i in range(xmax):
            for j in range(ymax):
                if grid[i][j] == 0:
                    count += 1
                    dfsCovertToWater(i, j)
        return count
