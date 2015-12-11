# Sort the list, O(nlogn)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums, reverse = True)
        return nums[k - 1]


# http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html
# Quick select algorithm, O(n) in average.
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pivot = random.choice(nums)
        large = []
        small = []
        for i in nums:
            if i > pivot:
                large.append(i)
            elif i < pivot:
                small.append(i)
        if len(large) >= k:
            return self.findKthLargest(large, k)
        elif k > len(nums) - len(small):
            return self.findKthLargest(small, k - (len(nums) - len(small)))
        else:
            return pivot