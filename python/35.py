# Pay attention to the edge cases, ([1] 1), ([1], 2).
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[-1] < target:
            return len(nums)
        for i in range(0, len(nums)):
            if nums[i] == target:
                return i
            elif nums[i] > target:
                return i