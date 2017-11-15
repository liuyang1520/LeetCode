"""
O(n)
left sum + pivot index value + right sum = total sum
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            if i >= 1:
                leftSum += nums[i-1]
            if 2 * leftSum + nums[i] == total:
                return i
        return -1
