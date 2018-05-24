"""
See better solutions: https://leetcode.com/problems/rectangle-overlap/solution/
"""
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        for x, y in [(rec1[0], rec1[1]), (rec1[0], rec1[3]), (rec1[2], rec1[1]), (rec1[2], rec1[3])]:
            if self.isInRectangle(rec2, x, y): return True
        for x, y in [(rec2[0], rec2[1]), (rec2[0], rec2[3]), (rec2[2], rec2[1]), (rec2[2], rec2[3])]:
            if self.isInRectangle(rec1, x, y): return True
        if self.isContain(rec1, rec2) or self.isContain(rec2, rec1): return True
        return False

    def isInRectangle(self, rec, x, y):
        return rec[0] < x and rec[1] < y and rec[2] > x and rec[3] > y

    def isContain(self, rec1, rec2):
        return rec1[0] <= rec2[0] and rec1[2] >= rec2[2] and rec1[1] >= rec2[1] and rec1[3] <= rec2[3]
