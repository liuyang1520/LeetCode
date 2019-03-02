"""
Get row max and column max, then find the min in both maxes
"""
class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowMax = [max(row) for row in grid]
        colMax = [max(grid[i][j] for i in range(len(grid))) for j in range(len(grid[0]))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rowMax[i], colMax[j]) - grid[i][j]
        return res
