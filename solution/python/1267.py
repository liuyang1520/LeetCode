"""
@difficulty: medium
@tags: misc
@notes: Only need to store how many servers are in the same rows and columns, then do another iteration for identifying isolations.
"""
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        from collections import defaultdict
        rows, columns = defaultdict(int), defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rows[i] += 1
                    columns[j] += 1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if rows[i] > 1 or columns[j] > 1:
                        res += 1
        return res
