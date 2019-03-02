"""
Stack, append smaller numbers, pop when larger numbers
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        size = len(nums)
        res = [-1] * size
        nums = nums + nums
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1][1] < nums[i]:
                index, value = stack.pop()
                res[index] = nums[i]
            if i < size:
                stack.append([i, nums[i]])
        return res
