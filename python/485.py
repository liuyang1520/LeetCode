"""
1. use a stack to store the 1s
or,
2. use a count variable to store the length only
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        storeList = []
        nums += [0]
        for i in nums:
            if not i:
                maxLength = max(maxLength, len(storeList))
                storeList = []
            else:
                storeList.append(i)
        return maxLength


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = 0
        length = 0
        nums += [0]
        for i in nums:
            if not i:
                maxLength = max(maxLength, length)
                length = 0
            else:
                length += 1
        return maxLength