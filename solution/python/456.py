"""
Use a stack, rightMinValue is the min value in the right part
3 6 6 4 5
stack = [5], rightMinValue = min_float
stack = [5, 4], rightMinValue = min_float
stack = [6], rightMinValue = 5, note the reverse order guarantees that this value is the max value in the right part
stack = [6, 6], rightMinValue = 5
3 < 5, return True
"""
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        rightMinValue = -float('inf')
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < rightMinValue:
                return True
            while stack and stack[-1] < nums[i]:
                rightMinValue = stack.pop()
            stack.append(nums[i])
        return False