# DP solution, get Time Limit Exceeded. O(n^2).
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        dp = [False] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            jumps = i + nums[i]
            if jumps >= len(nums) - 1:
                dp[i] = True
            else:
                while jumps > i:
                    dp[i] |= dp[jumps]
                    if dp[i]:
                        break
                    jumps -= 1
        return dp[0]


# Greedy solution. Jumps indicates how far can move from the current position. O(n).
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jumps = nums[0]
        for i in range(1, len(nums)):
            if jumps > 0:
                jumps -= 1
                jumps = max(jumps, nums[i])
            else:
                return False
        return True