"""
Max-min dp solution or
return True directly, as Alex will always win
"""
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        # dp[i][j] is the max of diff points for Alex - Lee
        length = len(piles)
        dp = [[-float('inf')] * length for i in range(length)]
        for i in range(length):
            dp[i][i] = -piles[i]
        turn = True
        for delta in range(1, length):
            for left in range(length - delta):
                right = delta + left
                if turn:
                    dp[left][right] = max(piles[left] + dp[left+1][right], piles[right] + dp[left][right-1])
                else:
                    dp[left][right] = min(-piles[left] + dp[left+1][right], -piles[right] + dp[left][right-1])
            turn ^= True
        return dp[0][length-1] > 0
