# Forgive my naughtiness :)
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)


# Binary search solution.
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        res = nums[0]
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] <= nums[high]:
                high = mid - 1
            else:
                low = mid + 1
            res = min(nums[mid], res)
        return res