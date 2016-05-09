# Use get Kth smallest num among two list. Recursively comparing the k / 2 in both lists, and drop smaller half list.
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length = len(nums1) + len(nums2)
        if length % 2 == 1:
            return self.getKthSmallest(nums1, nums2, length / 2 + 1)
        else:
            return (self.getKthSmallest(nums1, nums2, length / 2) + self.getKthSmallest(nums1, nums2, length / 2 + 1)) / 2.0
        
        
    def getKthSmallest(self, list1, list2, k):
        if len(list1) > len(list2):
            return self.getKthSmallest(list2, list1, k)
        if len(list1) == 0:
            return list2[k - 1]
        if k == 1:
            return min(list1[0], list2[0])
        half = min(k / 2, len(list1))
        if list1[half - 1] <= list2[k - half - 1]:
            return self.getKthSmallest(list1[half:], list2, k - half)
        else:
            return self.getKthSmallest(list1, list2[k - half:], half)