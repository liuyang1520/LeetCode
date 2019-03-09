"""
The hard part is to make sure each result has the same probability to be chosen.
For example, we have 3 numbers 2, 2, 2
The code below guarantees the same probability for each number:
1) first 2, 100% = res
2) second 2, 50% = res, so first 2 = 50%
3) third 2, 33.3% = res, first 2 = second 2 = 66.6% / 2 = 33.3%
which is very tricky.
"""
class Solution(object):
    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        from random import randint
        count = -1
        res = 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                count += 1
                if randint(0, count) == count:
                    res = i
        return res