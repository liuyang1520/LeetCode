# DP solution O(n^2), got Time Limit Exceeded
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0] * len(nums)
        for i in range(1, len(dp)):
            for j in range(0, i):
                if (not dp[i]) and nums[j] >= i - j:
                    dp[i] = dp[j] + 1
                elif dp[i] and nums[j] >= i - j and dp[j] + 1 < dp[i]:
                    dp[i] = dp[j] + 1
        return dp[-1]


# Greedy solution O(n)
"""
Find the max distance reachable under current limitation of steps.
jumps is the currenct jumps numbers,
distances is the currenct max distance can be reach without more jumps,
cover is the max distance can be reached.
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        distances = 0
        cover = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if i > distances:
                jumps += 1
                distances = cover
            walks = nums[i] + i
            if walks > cover:
                cover = walks
        return jumps