"""
Brute-force, be careful of the init value
"""
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest, secondlargest = (-1, -1), -1
        for i in range(len(nums)):
            if nums[i] > largest[0]:
                secondlargest = largest[0]
                largest = (nums[i], i)
            elif nums[i] > secondlargest:
                secondlargest = nums[i]
        if largest[0] >= 2 * secondlargest:
            return largest[1]
        else:
            return -1
