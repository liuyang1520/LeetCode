"""
@difficulty: easy
@tags: misc
@notes: Find the sum for target totalSum/3, then another target for totalSum*2/3.
"""
class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sums, subtotal = [], 0
        for i in A:
            subtotal += i
            sums.append(subtotal)
        if sums[-1] % 3: return False
        target = sums[-1] / 3
        i = j = -1
        for i in range(len(A)):
            if sums[i] == target:
                break
        for j in range(i+1, len(A)):
            if sums[j] == 2 * target:
                break
        if i < j < len(A) - 1:
            return True
        return False
