class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        sumA = sum(A)
        sumB = sum(B)
        counterB = Counter(B)
        for i in A:
            if i + (sumB - sumA) / 2 in counterB:
                return [i, i + (sumB - sumA) / 2]
