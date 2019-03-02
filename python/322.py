# DP problem
# f(x) is the min number of coins for amount x
# f(x) = min([f(x - i) + 1) for i in coins])
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for j in range(1, amount + 1):
            temp = 100000
            for i in coins:
                if j - i >= 0 and dp[j - i] >= 0:
                    temp = min(dp[j - i] + 1, temp)
            dp[j] = temp if temp != 100000 else -1
        return dp[-1]