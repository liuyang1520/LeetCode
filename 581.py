"""
1. Sort and compare
2. https://discuss.leetcode.com/topic/89282/java-o-n-time-o-1-space/20
"""
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortedNums = sorted(nums)
        left, right = 0, -1
        for i in range(len(nums)):
            if nums[i] != sortedNums[i]:
                left = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sortedNums[i]:
                right = i
                break
        return right - left + 1
