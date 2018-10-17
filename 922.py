"""
In-place two pointer solution.
"""
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, 1
        while i < len(A) and j < len(A):
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 2
                j += 2
            elif A[i] % 2 == 0 and A[j] % 2 == 1:
                i += 2
                j += 2
            elif A[i] % 2 == 0 and A[j] % 2 == 0:
                i += 2
            else:
                j += 2
        return A
