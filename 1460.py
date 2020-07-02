"""
@difficult: easy
@tags: misc
@notes: Only need to compare whether all the elements are same, since there is always a way to make these two equal.
"""
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
