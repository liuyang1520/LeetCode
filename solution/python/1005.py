"""
@difficulty: easy
@tags: misc
@notes: Sort the numbers and reverse the K negatives, if not enough, reverse the minimum positive to negative.
"""
class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        negs, posis = sorted([i for i in A if i < 0]), sorted([i for i in A if i > 0])
        if len(negs) >= K:
            return sum(posis) - sum(negs[:K]) + sum(negs[K:])
        rem = K - len(negs)
        allNums = sorted([abs(i) for i in A])
        if rem % 2 == 0:
            return sum(allNums)
        else:
            return sum(allNums) - 2 * allNums[0]
