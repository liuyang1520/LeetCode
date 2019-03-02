"""
Easy problem, use rows and maxWidth to track lines number and remaining width
"""
class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        maxWidth = 100
        rows = 1
        for i in S:
            index = ord(i) - 97
            if widths[index] <= maxWidth:
                maxWidth -= widths[index]
            else:
                maxWidth = 100 - widths[index]
                rows += 1
        return [rows, 100 - maxWidth]
