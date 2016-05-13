# String processing.
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = ["" for i in range(numRows)]
        row = 0
        column = 0
        for i in range(len(s)):
            res[row] += s[i]
            if column % (numRows - 1) == 0:
                row += 1
            else:
                column += 1
                row -= 1
            if row == numRows:
                row -= 2
                column += 1
        return "".join(res)
