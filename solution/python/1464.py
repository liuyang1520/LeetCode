"""
@difficulty: easy
@tags: misc
@notes: Sort, heap, Max+remove, find the two maximum values in a list.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        import heapq
        x, y = heapq.nlargest(2, nums)
        return (x - 1) * (y - 1)
