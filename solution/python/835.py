"""
For each pair of points, from A and B, calculate the x diff and y diff, use a set to store the value for key (x_diff, y_diff).
The max would be the max of the values in the set.
"""
class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        mapping = {}
        for xa in range(len(A)):
            for ya in range(len(A[0])):
                if A[xa][ya]:
                    for xb in range(len(B)):
                        for yb in range(len(B[0])):
                            if B[xb][yb]:
                                dx = xa - xb
                                dy = ya - yb
                                mapping[dx, dy] = mapping.get((dx, dy), 0) + 1
        return max(mapping.values() or [0])
