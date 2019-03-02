# Moving window solution
"""
[2,3,1,2,4,1], 7
[2,3,1,2] good
[3,1,2] bad
[3,1,2,4] good
[1,2,4] good
[2,4] bad
[2,4,1] good
min length is 3
"""
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left, right, total = 0, 0, 0
        res = len(nums) + 1
        while right < len(nums):
            while total < s and right < len(nums):
                total += nums[right]
                right += 1
            while total >= s and left < right:
                res = min(res, right - left)
                if res == 1: return 1
                total -= nums[left]
                left += 1
        return 0 if res == len(nums) + 1 else res