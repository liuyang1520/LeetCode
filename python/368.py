"""
DP, dp[i] = max(dp[i], dp[j] + 1) for j in range(0, i) and nums[i] % nums[j] == 0
Use trace to trace the elements
"""
class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        dp = [1] * (len(nums) + 1)
        trace = {}
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    trace[i] = j
        res = []
        maxIndex = dp.index(max(dp))
        while dp[maxIndex] > 1:
            res.append(nums[maxIndex])
            maxIndex = trace[maxIndex]
        res.append(nums[maxIndex])
        return res