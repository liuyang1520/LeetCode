"""
@difficulty: easy
@tags: misc
@notes: Iterate list from left to right.
"""
class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3 or A[0] > A[1]: return False
        increasing = True
        for i in range(1, len(A)):
            if A[i] > A[i-1] and increasing:
                continue
            elif A[i] < A[i-1] and increasing:
                increasing = False
            elif A[i] < A[i-1] and not increasing:
                continue
            else:
                return False
        if not increasing:
            return True
        return False
