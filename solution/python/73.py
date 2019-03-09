# Space complexity O(n), to indicate which column should be zeros
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        stat = [0] * len(matrix[0])
        for i in range(len(matrix)):
            hasZero = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    hasZero = True
                    stat[j] = 1
            if hasZero:
                matrix[i][:] = [0] * len(matrix[i])
        for i in range(len(stat)):
            if stat[i]:
                for m in range(len(matrix)):
                    matrix[m][i] = 0


# Found that the first row can be used instead to make space complexity O(c).
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        firstRowZero = False
        if 0 in matrix[0]:
            firstRowZero = True
        for i in range(len(matrix)):
            hasZero = False
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    hasZero = True
                    matrix[0][j] = 0
            if hasZero and i > 0:
                matrix[i] = [0] * len(matrix[i])
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                for m in range(len(matrix)):
                    matrix[m][i] = 0
        if firstRowZero:
            matrix[0] = [0] * len(matrix[0])