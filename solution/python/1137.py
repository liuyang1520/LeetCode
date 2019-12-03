"""
@difficulty: easy
@tags: misc
@notes: Intuitive solution.
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0, 1, 1]
        if n <= 2:
            return nums[n]
        for i in range(n-2):
            subsum = sum(nums)
            nums = nums[1:] + [subsum]
        return nums[-1]
