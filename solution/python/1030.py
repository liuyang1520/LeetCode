"""
@difficulty: easy
@tags: misc
@notes: Sort by distance.
"""
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        cells = [(i, j) for i in range(R) for j in range(C)]
        return sorted(cells, key = lambda x: abs(x[0] - r0) + abs(x[1] - c0))
