"""
@difficulty: medium
@tags: DP, DFS
@notes: f(i, m) = max(sum(piles[i: i + d]) - f(i + d, max(m, d))) (1 <= d <= 2*m), is the max diff stores Alex - Lee from i, m position.
"""
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        from functools import lru_cache
        length = len(piles)
        @lru_cache(None)
        def helper(i, m):
            maxIndex = i + 2 * m
            if maxIndex >= length:
                return sum(piles[i:])
            maxValue = float('-inf')
            for j in range(i+1, maxIndex+1):
                maxValue = max(maxValue, sum(piles[i: j]) - helper(j, max(m, j-i)))
            return maxValue
        return (sum(piles) + helper(0, 1)) // 2
