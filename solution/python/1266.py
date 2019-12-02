"""
@difficulty: easy
@tags: misc
@notes: max(abs(x1 - x0), abs(y1 - y0)) is the diff between nodes.
"""
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total = 0
        x0, y0 = points[0]
        for i in range(1, len(points)):
            x1, y1 = points[i]
            total += max(abs(x1 - x0), abs(y1 - y0))
            x0, y0 = x1, y1
        return total
