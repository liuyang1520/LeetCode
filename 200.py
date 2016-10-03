"""
DFS, for each point, mark it "#" if it is 1.
"""
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        
        x_max, y_max = len(grid), len(grid[0])
        def dfs(x, y):
            for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if 0 <= i < x_max and 0 <= j < y_max and grid[i][j] == "1":
                    grid[i][j] = "#"
                    dfs(i, j)
        
        res = 0
        for i in range(x_max):
            for j in range(y_max):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res