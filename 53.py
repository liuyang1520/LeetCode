# If the sum is minus zero, start from new position again
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        if len(nums) == 1:
            return nums[0]
        res = max(nums)
        for i in range(len(nums)):
            total += nums[i]
            if total <= 0:
                total = 0
            else:
                res = max(total, res)
        return res