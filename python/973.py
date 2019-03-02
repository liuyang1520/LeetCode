"""
@difficulty: easy
@tags: misc
@notes: Sort the distances then fetch the first K records.
"""
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distances = [[point[0]**2 + point[1]**2, point] for i, point in enumerate(points)]
        return map(lambda x: x[1], sorted(distances)[:K])
