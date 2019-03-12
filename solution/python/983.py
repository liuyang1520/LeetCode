"""
@difficulty: medium
@tags: DP
@notes: dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])
"""
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [float('inf')] * (max(days) + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0], dp[max(i-7, 0)] + costs[1], dp[max(i-30, 0)] + costs[2])
        return dp[-1]
