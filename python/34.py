# Use two binary search to find the start and end points of the range.
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        res = [-1, -1]
        while start < end:
            mid = (start + end) / 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        if nums[start] != target:
            return res
        else:
            res[0] = start
        end = len(nums) - 1
        while start < end:
            mid = (start + end + 1) / 2
            if nums[mid] != target:
                end = mid - 1
            else:
                start = mid
        res[1] = end
        return res