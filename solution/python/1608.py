"""
@difficulty: easy
@tags: misc
@notes: this solution is slow, check
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/discuss/877722/Clean-Python-3-O(sort)
"""
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        length = len(nums)
        stats = [0] * (length + 1)
        for num in nums:
            for i in range(0, min(num + 1, length + 1)):
                stats[i] += 1
        for i in range(1, len(stats)):
            if i == stats[i]:
                return i
        return -1
