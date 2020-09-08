"""
@difficulty: medium
@tags: greedy
@notes: always pick up the second largest value from the list
"""
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        start = len(piles) // 3
        for i in range(start, len(piles), 2):
            res += piles[i]
        return res
