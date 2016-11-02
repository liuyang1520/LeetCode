"""
Since no extra space is allowed, we need to use the nums list to mark whether a num appears twice.
"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                res += [abs(nums[i])]
            else:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
        return res