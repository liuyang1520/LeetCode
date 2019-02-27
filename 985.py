"""
@difficulty: easy
@tags: misc
@notes: Got TLE if recalculate the sum from scratch each time, need to updateh sum for each query.
"""
class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        init = sum(i for i in A if i % 2 == 0)
        res = []
        for val, i in queries:
            if A[i] % 2 == 0:
                init -= A[i]
            A[i] += val
            if A[i] % 2 == 0:
                init += A[i]
            res.append(init)
        return res
