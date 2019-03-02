"""
O(n), do a iteration and reset a temp variable whenever direction is false
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0
        i = 0
        while i < len(nums) - 1:
            subLen = 1
            while i < len(nums) - 1 and nums[i+1] > nums[i]:
                subLen += 1
                i = i + 1
            maxLen = max(maxLen, subLen)
            i += 1
        if len(nums) <= 1:
            return len(nums)
        else:
            return maxLen
