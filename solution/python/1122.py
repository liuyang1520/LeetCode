"""
@difficulty: easy
@tags: sort
@notes: Sort by the index of elements.
"""
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        mapping = dict((val, i) for i, val in enumerate(arr2))
        def keyHelper(x):
            if x in mapping:
                return mapping[x]
            return 1000 + x
        return sorted(arr1, key=keyHelper)
