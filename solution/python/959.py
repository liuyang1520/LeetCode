"""
@difficulty: medium
@tags: DFS, graph
@notes: Use a 3*3 upscale graph to represent a slash grid, cannot use 2*2 as only 4-directions. Then run a DFS.
"""
class Solution(object):
    def regionsBySlashes(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        newGrid = [[1] * len(grid) * 3 for i in range(len(grid) * 3)]
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == '/':
                    newGrid[3*i][3*j+2] = 0
                    newGrid[3*i+1][3*j+1] = 0
                    newGrid[3*i+2][3*j] = 0
                if grid[i][j] == '\\':
                    newGrid[3*i][3*j] = 0
                    newGrid[3*i+1][3*j+1] = 0
                    newGrid[3*i+2][3*j+2] = 0
        delta = ([-1, 0], [1, 0], [0, -1], [0, 1])
        total = [0]

        def dfs(i, j, count):
            if newGrid[i][j] != 1:
                return
            newGrid[i][j] = 2
            total[0] += count
            for dx, dy in delta:
                x, y = i + dx, j + dy
                if 0 <= x < len(newGrid) and 0 <= y < len(newGrid) and newGrid[x][y] == 1:
                    dfs(x, y, 0)

        for i in range(len(newGrid)):
            for j in range(len(newGrid)):
                dfs(i, j, 1)
        return total[0]
