# Use dictionary to store the values. Or use set() alternatively.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numsDict = {}
        for i in nums:
            if i not in numsDict:
                numsDict[i] = 1
            else:
                return True
        return False