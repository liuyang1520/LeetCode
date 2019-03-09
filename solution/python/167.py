"""
Use two pointers, left and right, to dynamically update values
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers)-1
        while left < right:
            subsum = numbers[left] + numbers[right]
            if subsum == target:
                return [left + 1, right + 1]
            elif subsum > target:
                right -= 1
            else:
                left += 1