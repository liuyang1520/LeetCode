"""
@difficulty: easy
@tags: misc
@notes: calculate when first encounter the key.
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(nums)
        stats = {}
        for i, val in enumerate(sortedNums):
            if val not in stats:
                stats[val] = i
        return [stats[i] for i in nums]
