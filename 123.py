# DP solution, res[i][j] is max profit from day i to day j. res[0][end2] = for end1:end2 -> max(res[0][end1] + res[en1][end2]).
# However, it is running out of time.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.prices = prices
        days = len(prices)
        if days <= 1:
            return 0
        res = [[0] * days] * days
        res[0][1] = max(prices[1] - prices[0], 0)
        for i in range(1, days):
            for j in range(i + 1, days):
                res[0][j] = max(res[0][i] + self.maxProfitInterval(i, j), res[0][j])
        return res[0][days - 1]
        
        
    def maxProfitInterval(self, e1, e2):
        maxP = 0
        count = 0
        for i in range(e1, e2):
            count += self.prices[i + 1] - self.prices[i]
            if count > maxP:
                maxP = count
            if count < 0:
                count = 0
        return maxP


# DP solution. p1[i] is the max profit before day i, p2[i] is the max profit after day i. The sum is the total profit.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        days = len(prices)
        if days <= 1:
            return 0
        p1 = [0] * days
        count1 = 0
        for i in range(0, days - 1):
            count1 += prices[i + 1] - prices[i]
            p1[i + 1] = max(count1, p1[i])
            if count1 < 0:
                count1 = 0
        count2 = 0
        p2 = [0] * days
        for j in range(days - 1, 0, -1):
            count2 += prices[j] - prices[j - 1]
            p2[j - 1] = max(p2[j], count2)
            if count2 < 0:
                count2 = 0

        maxP = 0
        for i in range(0, days):
            maxP = max(p1[i] + p2[i], maxP)
        return maxP
