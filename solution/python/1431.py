"""
@difficulty: easy
@tags: misc
@notes: naive solution.
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        return map(lambda x: x + extraCandies >= maxCandy, candies)
