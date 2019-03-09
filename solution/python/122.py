# If it is increasing, then add to the profit. Else ignore it.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell = 0
        buy = 0
        profit = 0
        if prices == None:
            return 0
        for sell in range(len(prices)):
            if prices[sell] > prices[buy]:
                profit += prices[sell] - prices[buy]
            buy = sell
        return profit