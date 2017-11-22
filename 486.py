"""
1. Recusive solution
2. DP solution
Ideas are same, when player 1 picks, picks the largest, when player 2 picks, picks the largest too, so nums[0] - helper(nums[1:]).
Since the value for player 2 is not good for player 1.
dp[i][j] means the best value from index i to index j of nums, for player 1
The dp solution updates the values by slide length.
"""
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memories = {}
        def helper(nums):
            if len(nums) <= 1:
                return sum(nums)
            numsTuple = tuple(nums)
            if numsTuple in memories:
                return memories[numsTuple]
            temp = max(nums[0] - helper(nums[1:]), nums[-1] - helper(nums[:-1]))
            memories[numsTuple] = temp
            return temp
        return helper(nums) >= 0


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [[0] * len(nums) for i in range(len(nums))]
        for i in range(len(nums)):
            dp[i][i] = nums[i]
        for slideLength in range(1, len(nums)):
            for i in range(0, len(nums) - slideLength):
                j = i + slideLength
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])
        return dp[0][-1] >= 0
