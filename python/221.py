'''
f(x, y) is the longest edge of square contains x, y point.
f(x, y) = min(f(x-1, y-1), f(x-1, y), f(x, y-1)) + 1
Only x - 1 >= 0, y - 1 >=0, the result is valid.
'''
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        maxArea = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) and i > 0 and j > 0:
                    matrix[i][j] = min(int(matrix[i-1][j-1]), int(matrix[i-1][j]), int(matrix[i][j-1])) + 1
                maxArea = max(maxArea, int(matrix[i][j]))
        return maxArea ** 2