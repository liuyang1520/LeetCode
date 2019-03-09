class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        total = 0
        total += sum(1 if val else 0 for row in grid for val in row)
        total += sum(max(row) for row in grid)
        for col in range(len(grid[0])):
            total += max(grid[i][col] for i in range(len(grid)))
        return total
