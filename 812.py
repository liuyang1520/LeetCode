"""
Heron's formula
"""
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        maxArea = 0
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                for k in range(j+1, len(points)):
                    maxArea = max(maxArea, self.triangleArea(points[i], points[j], points[k]))
        return maxArea

    def triangleArea(self, p1, p2, p3):
        a = self.distance(p1, p2)
        b = self.distance(p1, p3)
        c = self.distance(p2, p3)
        s = (a + b + c) / 2.0
        if s < a or s < b or s < c:
            return 0
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    def distance(self, p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
