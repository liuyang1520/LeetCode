"""
1. Use Counter to get the max frequency number
2. Use a hash to know the leftmost and rightmost value for each value
It seems that Counter is slow comparing to manually getting the count via dictionary
"""
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        counter = Counter(nums)
        minLen = float('inf')
        maxCount = counter.most_common(1)[0][1]
        positions = {}
        for i in range(len(nums)):
            if nums[i] in positions:
                positions[nums[i]]['right'] = i
            if nums[i] not in positions:
                positions[nums[i]] = {'left': i, 'right': i}
        for i in counter:
            if counter[i] == maxCount:
                minLen = min(minLen, positions[i]['right'] - positions[i]['left'] + 1)
        return minLen
