"""
Math problem
for each discontinuous 1s, we count 2 units for the perimeter
"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        xmax, ymax = len(grid), len(grid[0])
        for x in range(xmax):
            for y in range(ymax):
                if grid[x][y] and (y == 0 or not grid[x][y-1]):
                    count += 1
                if grid[x][y] and (x == 0 or not grid[x-1][y]):
                    count += 1
        return count * 2