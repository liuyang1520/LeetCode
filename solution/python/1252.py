"""
@difficulty: easy
@tags: misc
@notes: Create a 2D array for simulation.
Another option would be just counting the row, column numbers, and sum all for odd times rows/columns.
"""
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        nums = [[0] * m for i in range(n)]
        for row, col in indices:
            # Update row
            for j in range(m):
                nums[row][j] += 1
            # Update column
            for i in range(n):
                nums[i][col] += 1
        res = 0
        for row in nums:
            for num in row:
                if num % 2:
                    res += 1
        return res
