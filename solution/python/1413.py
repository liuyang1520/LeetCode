"""
@difficulty: easy
@tags: misc
@notes: Iterate the array to get the min subsum.
"""
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minSum = float('inf')
        subsum = 0
        for i in nums:
            subsum += i
            minSum = min(minSum, subsum)
        return max(1, -minSum + 1)
