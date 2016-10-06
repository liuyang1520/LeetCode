"""
Create 2d subsums:
subSums[x][y] = subSums[x-1][y] + subSums[x][y-1] - subSums[x-1][y-1] + matrix[x-1][y-1]

Return result:
subSums[row2+1][col2+1] - subSums[row1][col2+1] - subSums[row2+1][col1] + subSums[row1][col1]
"""
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        x_max, y_max = len(matrix), len(matrix[0])
        self.subSums = [[0] * (y_max + 1) for i in range(x_max + 1)]
        for x in range(1, x_max + 1):
            for y in range(1, y_max + 1):
                self.subSums[x][y] = self.subSums[x-1][y] + self.subSums[x][y-1] - self.subSums[x-1][y-1] + matrix[x-1][y-1]
        print self.subSums
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.subSums[row2+1][col2+1] - self.subSums[row1][col2+1] - self.subSums[row2+1][col1] + self.subSums[row1][col1]