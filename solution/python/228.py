# Easy string operation
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if not nums:
            return res
        i = 0
        while i < len(nums):
            start = end = nums[i]
            j = i + 1
            while j < len(nums) and nums[j] == nums[j-1] + 1:
                j += 1
            end = nums[j-1]
            if start == end:
                res.append(str(start))
            else:
                res.append(str(start) + "->" + str(end))
            i = j
        return res