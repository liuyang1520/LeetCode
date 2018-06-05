class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import Counter
        groups = [-1, 0, 1]
        count = 0
        for i in range(1, len(grid) - 1):
            for j in range(1, len(grid[0]) - 1):
                numbers = [grid[i+dx][j+dy] for dx in groups for dy in groups]
                if len(Counter(numbers)) != 9 or any(s > 9 or s < 1 for s in numbers):
                    continue
                subsum = grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1]
                isMagic = True
                for dx in groups:
                    if sum(grid[i+dx][j+dy] for dy in groups) != subsum:
                        isMagic = False
                        break
                for dy in groups:
                    if sum(grid[i+dx][j+dy] for dx in groups) != subsum:
                        isMagic = False
                        break
                if (subsum - grid[i][j] != grid[i-1][j-1] + grid[i+1][j+1]) or (subsum - grid[i][j] != grid[i-1][j+1] + grid[i+1][j-1]):
                    isMagic = False
                if isMagic:
                    count += 1
        return count
