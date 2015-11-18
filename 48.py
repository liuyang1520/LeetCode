# Just need to operate on 1/4 of the whole image.
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range((size+1) / 2):
            for j in range(size / 2):
                matrix[i][j], matrix[size-1-j][i], matrix[size-1-i][size-1-j], matrix[j][size-1-i] = (
                matrix[size-1-j][i],
                matrix[size-1-i][size-1-j],
                matrix[j][size-1-i],
                matrix[i][j]
                )