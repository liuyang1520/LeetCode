"""
Recursive + memorization.
There is DP solution for this.
"""
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        self.coins = sorted(filter(lambda x: x<=amount, coins), reverse=True)
        if amount == 0: return 1
        if not coins: return 0
        self.memorize = {}
        return self.helper(amount, 0)

    def helper(self, value, index):
        if value == 0:
            return 1
        if index == len(self.coins) - 1:
            if (value % self.coins[-1]) == 0:
                return 1
            else:
                return 0
        if (value, index) in self.memorize:
            return self.memorize[(value, index)]
        res = 0
        if value >= self.coins[index]: res = self.helper(value-self.coins[index], index)
        res += self.helper(value, index+1)
        self.memorize[(value, index)] = res
        return res
