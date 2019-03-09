# Use a pointer pointing to non-duplicated numbers location, if duplicate, switch next to current.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pos = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[pos]:
                nums[i], nums[pos + 1] = nums[pos + 1], nums[i]
                pos += 1
        return pos + 1