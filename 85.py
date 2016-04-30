# This problem is an ungrade version of problem 84.
# Scan each row in the matrix, and transfer it to a 1-D histogram. Then use the solution in 84 to solve it.
# Example:
# 1 1 0 1
# 0 1 0 0
# 1 0 1 1
# 1 0 1 0
# 1) histList: row1->[1, 1, 0, 1]
# 2) histList: row1->[1, 1, 0, 1], row2->[0, 2, 0, 0]
# 3) histList: row1->[1, 1, 0, 1], row2->[0, 2, 0, 0], row3->[1, 0, 1, 1]
# 4) histList: row1->[1, 1, 0, 1], row2->[0, 2, 0, 0], row3->[1, 0, 1, 1], row4->[2, 0, 2, 0]


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        res = 0
        if not matrix:
            return res
        rows = len(matrix)
        columns = len(matrix[0])
        histList = [[0] * columns]
        for i in range(rows):
            temp = []
            for j in range(columns):
                if matrix[i][j] == "0":
                    temp.append(0)
                else:
                    temp.append(1 + histList[i][j])
            histList.append(temp)
        for i in range(len(histList)):
            res = max(res, self.largestRectangleArea(histList[i]))
        return res
        
    def largestRectangleArea(self, heights):
        res = 0
        if len(heights) == 1:
            return heights[0]
        stack = [(0, 0)]  # height and index
        for pos in range(len(heights)):
            if heights[pos] > stack[-1][0]:
                stack.append((heights[pos], pos))
            elif heights[pos] < stack[-1][0]:
                while heights[pos] < stack[-1][0]:
                    last = stack.pop()
                    res = max(res, last[0] * (pos - last[1]))
                stack.append((heights[pos], last[1]))
        while stack:
            last = stack.pop()
            res = max(res, last[0] * (len(heights) - last[1]))
        return res