"""
Binary search on sorted array, need to separate cases when number of half is even or odd
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if right - left == 2:
                return nums[left] ^ nums[left+1] ^ nums[right]
            if (mid - left + 1) % 2:
                if nums[mid-1] == nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid-1] == nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
