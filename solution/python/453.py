"""
1,2,5,6
2,2,6,7
6,6,6,11
11,11,11,11
sum(nums) - min(nums) * len(nums)
"""
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - min(nums) * len(nums)