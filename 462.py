"""
pick up the mid position value as the base, and calculate distance from it
"""
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = nums[len(nums) / 2]
        count = 0
        for j in nums:
            count += abs(i - j)
        return count