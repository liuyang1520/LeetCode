# Insert from the start of nums1. Not actually in-place solution.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, length = 0, 0, m
        while i <= length - 1 and j <= n - 1:
            if nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1.insert(i, nums2[j])
                i += 1
                j += 1
                length += 1
        if i > length - 1:
            nums1[i:] = nums2[j:]
        nums1[:] = nums1[0 : m+n]


# Insert from the end of nums1, in-place solution.
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j, length = m - 1, n - 1, m + n -1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[length] = nums2[j]
                j -= 1
            else:
                nums1[length] = nums1[i]
                i -= 1
            length -= 1
        if i < 0:
            for s in range(0, j + 1):
                nums1[s] = nums2[s]
        