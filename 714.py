"""
DP, profit is the max money can get today, remains is the money after purchasing today's stock
"""
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        profit, remains = 0, -prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, remains + prices[i] - fee)
            remains = max(remains, profit - prices[i])
        return profit
