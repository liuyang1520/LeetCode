# DP problem. Refer to http://www.hrwhisper.me/leetcode-burst-balloons/.
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        dp = [[0] * len(nums) for i in xrange(len(nums))]
        
        for k in xrange(2, len(nums)):
            for l in xrange(0, len(nums) - k):
                r = l + k
                for m in xrange(l + 1, r):
                    dp[l][r] = max(dp[l][r], nums[l]*nums[m]*nums[r] + dp[l][m] + dp[m][r])
        return dp[0][len(nums) - 1]