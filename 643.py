"""
O(n), slice window, add new number, minus old number
"""
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        maxsum = -float('inf')
        subsum = 0
        i = 0
        while i < len(nums):
            subsum += nums[i]
            if i >= k:
                subsum -= nums[i - k]
            if i >= k - 1 and subsum > maxsum:
                maxsum = subsum
            i += 1
        return maxsum / float(k)
