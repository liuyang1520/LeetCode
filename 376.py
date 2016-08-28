"""
Find the points of inflection, merge numbers into a segment with the same montonicity.
For example,
+++---++-+++ -> + - + - + -> 5
"""
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        diff = nums[1] - nums[0]
        res = 2 if diff else 1
        for i in range(2, len(nums)):
            diff_new = nums[i] - nums[i - 1]
            if diff_new != 0 and diff * diff_new <= 0:
                res += 1
                diff = diff_new
        return res