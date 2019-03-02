"""
x is the smallest value, y is the second smallest value
"""
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = y = float('inf')
        for i in nums:
            if i < x:
                x = i
            elif x < i < y:
                y = i
            elif i > y:
                return True
        return False