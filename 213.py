# DP problem.
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        # Choose the first element.
        dp1 = [0] * (len(nums) - 1)
        dp1[0] = dp1[1] = nums[0]
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i-2] + nums[i], dp1[i-1])
        # Not choose the first element.
        dp2 = [0] * len(nums)
        dp2[1] = nums[1]
        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i-2] + nums[i], dp2[i-1])
        return max(dp1[-1], dp2[-1])