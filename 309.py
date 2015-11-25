# sell and buy are max total profit when not holding or holding stock on i-th day.
# sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
# buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = [0] * len(prices)
        buy = [0] * len(prices)
        if len(prices) <= 1:
            return 0
        sell[0], sell[1] = 0, max(0, prices[1] - prices[0])
        buy[0], buy[1] = -prices[0], max(-prices[0], -prices[1])
        for i in range(2, len(prices)):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
        return sell[-1]