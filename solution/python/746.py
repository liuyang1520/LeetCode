"""
Standard DP problem
"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        dp = [float('inf')] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return dp[-1]
