class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        rowLen, colLen = len(A), len(A[0])
        transpose = [[0]*rowLen for i in range(colLen)]
        for x in range(rowLen):
            for y in range(colLen):
                transpose[y][x] = A[x][y]
        return transpose
