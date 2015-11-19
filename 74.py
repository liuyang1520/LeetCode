# Binary search, transfer 2D to 1D.
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        length = len(matrix) * len(matrix[0])
        width = len(matrix[0])
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) / 2
            if target < matrix[mid / width][mid % width]:
                right = mid - 1
            elif target > matrix[mid / width][mid % width]:
                left = mid + 1
            else:
                return True
        return False