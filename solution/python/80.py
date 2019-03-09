# Use a pointer pos pointing to the last in-duplicated sequence. Compare the pos - 1 element with new element.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return len(nums)
        pos = 1
        for i in range(2, len(nums)):
            if nums[pos - 1] != nums[i]:
                pos += 1
                nums[pos], nums[i] = nums[i], nums[pos]
        return pos + 1