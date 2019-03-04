"""
@difficulty: easy
@tags: greedy
@notes: Sort the list, then always pick up the largest 3 numbers with a moving pointer.
"""
class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        length = len(A)
        for i in range(length - 2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
