"""
@difficulty: easy
@tags: misc
@notes: brute-force.
"""
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        while numBottles >= numExchange:
            res += numBottles // numExchange
            numBottles = (numBottles % numExchange) + numBottles // numExchange
        return res
