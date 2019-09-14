"""
@difficulty: medium
@tags: misc
@notes: Intuitively count the frequency in both A and B, find the most common one, go through A and B again to check whether feasible.
"""
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        from collections import Counter
        length = len(A)
        counter = Counter(A) + Counter(B)
        common, freq = counter.most_common(1)[0]
        if freq < length:
            return -1
        for i in range(length):
            if A[i] != common and B[i] != common:
                return -1
        return min(length - A.count(common), length - B.count(common))
