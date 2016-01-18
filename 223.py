# S(A or B) = S(A) + S(B) - S(A and B)
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        areaOverlap = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
        return area1 + area2 - areaOverlap