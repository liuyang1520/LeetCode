"""
Compare to the top-left most element
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                temp = min(i, j)
                if matrix[i][j] != matrix[i-temp][j-temp]:
                    return False
        return True
