"""
For each bit in integer, from left to right, find whether the other part is in the set.
This guarantees that the maximum number gets returned.
"""
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = mask = 0
        for i in range(32, -1, -1):
            mask = mask | 1 << i
            prefixSet = set(num & mask for num in nums)
            temp = res | 1 << i
            for pre in prefixSet:
                if pre ^ temp in prefixSet:
                    res = temp
                    break
        return res