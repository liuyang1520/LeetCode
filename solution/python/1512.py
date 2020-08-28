"""
@difficulty: easy
@tags: misc
@notes: combination count.
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from collections import Counter
        counter = Counter(nums)
        res = 0
        for v in counter.values():
            if v >= 2:
                res += v * (v - 1) // 2
        return res
