"""
@difficulty: easy
@tags: misc
@notes: Hard to understand the question, moving the chips actually means increase or decrease the number at the same position.
"""
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        odds = sum(1 if i % 2 else 0 for i in chips)
        return min(odds, len(chips) - odds)
