"""
@difficulty: medium
@tags: misc
@notes: O(n)
"""
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i+1]:
                break
        else:
            return A
        maxIndex, maxVal = i, 0
        for j in range(i, len(A)):
            if A[j] < A[i] and A[j] > maxVal:
                maxIndex = j
                maxVal = A[j]
        A[i], A[maxIndex] = A[maxIndex], A[i]
        return A
