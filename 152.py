# Store the largest positive and min negative num from the start to current number. DP solution.
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        maxPos, minNeg = nums[0], nums[0]
        for i in range(1, len(nums)):
            maxTemp, minTemp = maxPos, minNeg
            if nums[i] >= 0:
                maxPos = max(maxTemp * nums[i], nums[i])
                minNeg = min(minNeg * nums[i], nums[i])
            else:
                maxPos = max(minTemp * nums[i], nums[i])
                minNeg = min(maxTemp * nums[i], nums[i])
            if maxPos > res:
                res = maxPos
        return res