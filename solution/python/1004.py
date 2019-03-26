"""
@difficulty: medium
@tags: slide window
@notes: Use slide window to maintain the max window size of ones.
"""
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i, j = 0, -1
        while j < len(A) - 1:
            if A[j+1] and K >= 0:
                j += 1
            elif not A[j+1] and K > 0:
                K -= 1
                j += 1
            else:
                i += 1
                j += 1
                if not A[j]:
                    K -= 1
                if not A[i-1]:
                    K += 1
        return j - i + 1
