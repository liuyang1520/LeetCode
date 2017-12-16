"""
DP solution:
1. get a dictionary of totoal sum for each value
2. dp[i] = max(dp[i-1], dp[i-2] + stats[i])
"""
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        from collections import defaultdict
        stats = defaultdict(int)
        for i in nums:
            stats[i] += i
        dp = [0] * (max(stats.values()) + 1)
        dp[1] = stats[1]
        for i in range(2, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + stats[i])
        return dp[-1]
