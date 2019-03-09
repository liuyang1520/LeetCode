"""
@difficulty: medium
@tags: misc
@notes: Use two pointers to iterate the lists in order.
"""
class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[Interval]
        :type B: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        i = j = 0
        while i < len(A) and j < len(B):
            if A[i].start > B[j].end:
                j += 1
            elif A[i].end < B[j].start:
                i += 1
            else:
                res.append([max(A[i].start, B[j].start), min(A[i].end, B[j].end)])
                if A[i].end >= B[j].end:
                    j += 1
                else:
                    i += 1
        return res
