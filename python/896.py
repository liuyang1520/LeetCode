"""
1. Sort and compare
2. Two passes for <= and >=
3. One pass with storing previous values
"""
class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return sorted(A) == A or sorted(A, reverse=True) == A
