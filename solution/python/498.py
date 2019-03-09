"""
1 2 3 4
5 6 7 8
9 a b c
"""
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        M, N = len(matrix), len(matrix[0])
        x, y, direct = 0, 0, 'NE'
        res = []
        while x < M and y < N:
            res.append(matrix[x][y])
            if direct == 'NE':
                if x >= 1 and y+1 < N:
                    x -= 1
                    y += 1
                elif x < 1 and y+1 < N:
                    y += 1
                    direct = 'SW'
                elif y+1 >= N:
                    x += 1
                    direct = 'SW'
            else:
                if x+1 < M and y >= 1:
                    x += 1
                    y -= 1
                elif x+1 >= M:
                    y += 1
                    direct = 'NE'
                elif x+1 < M and y < 1:
                    x += 1
                    direct = 'NE'
        return res
