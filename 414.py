"""
Use a list to store the max 3 numbers
"""
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxThree = []
        for i in nums:
            if i not in maxThree:
                if len(maxThree) < 3:
                    maxThree.append(i)
                    maxThree.sort()
                elif i > maxThree[0]:
                    maxThree.append(i)
                    maxThree = sorted(maxThree)[1:]
        if len(maxThree) < 3:
            return maxThree[-1]
        else:
            return maxThree[0]