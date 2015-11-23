# DP problem. f(n) = max(f(n-1), f(n-2)+c_n).
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * (len(nums) + 2)
        dp[0] = dp[1] = 0
        for i in range(len(nums)):
            dp[i+2] = max(dp[i] + nums[i], dp[i+1])
        return dp[len(nums) + 1]