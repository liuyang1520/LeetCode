# Mark appeared numbers to be negative in the corresponding locations
# Iterate the list again to pull out results
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in nums:
            nums[abs(i)-1] = -abs(nums[abs(i)-1])
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res