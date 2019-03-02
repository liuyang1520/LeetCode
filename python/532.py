"""
Use set to save time
"""
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import Counter
        pairs = set()
        counter = Counter(nums)
        if k < 0:
            return 0
        if k == 0:
            return len([i for i in counter if counter[i] >= 2])
        for i in counter:
            if i + k in counter:
                pairs.add((i, i + k))
        return len(pairs)
