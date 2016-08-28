# Use hashmap to store the values
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numsDict = {}
        for i in nums1:
            if i not in numsDict:
                numsDict[i] = 1
        for i in nums2:
            if i in numsDict:
                numsDict[i] = 2
        return filter(lambda x: numsDict[x] == 2, numsDict.keys())