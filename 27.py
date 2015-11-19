# Python list has remove method, or using filter.
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # Method 1
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)
        
        # Method 2
        nums[:] = list(filter(lambda x: x != val, nums))
        return len(nums)