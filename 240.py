# Method 1, brute force O(m*n).
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if target in i:
                return True
        return False


# Method 2, traversal in each row, use the sorted list to avoid comparisons, O(m + n).
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        col = len(matrix[0]) - 1
        for i in range(len(matrix)):
            while col > 0 and matrix[i][col] > target:
                col -= 1
            if matrix[i][col] == target:
                return True
        return False