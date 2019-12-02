"""
@difficulty: easy
@tags: misc
@notes: Copy the array for helping shifting.
"""
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        size = n * m
        if k == size:
            return grid
        copy = [[grid[i][j] for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                index = i * m + j
                index1 = (index + k) % size
                i1, j1 = index1 // m, index1 % m
                copy[i1][j1] = grid[i][j]
        return copy
