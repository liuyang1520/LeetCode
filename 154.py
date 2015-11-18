# The previous solution doesn't work for cases: [3 3 3 1 3] [3 1 3 3 3]
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # left = 0
        # right = len(nums) - 1
        # res = nums[0]
        # while left <= right:
        #     mid = (left + right) / 2
        #     if nums[mid] > nums[right]:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        #     res = min(res, nums[mid])
        # return res
        return min(nums)