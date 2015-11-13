# Use the idea of finding maximum subsequences. However, finding the lowest price may be a nicer alternative.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProf = 0
        if len(prices) <= 1:
            return maxProf
        temp = 0
        for i in range(1, len(prices)):
            if temp + prices[i] - prices[i - 1] >= 0:
                temp += prices[i] - prices[i - 1]
            else:
                temp = 0
            maxProf = max(maxProf, temp)
        return maxProf