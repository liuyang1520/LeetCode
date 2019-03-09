"""
1. Calculate and sort
2. Two pointers
Note sorted(<type 'generator'>) is slower than sorted(<type 'list'>)
https://stackoverflow.com/questions/4154571/sorted-using-generator-expressions-rather-than-lists
"""
class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i**2 for i in A])
