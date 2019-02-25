"""
The code can be simplified with nested loops.
"""
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        x, y = 0, 0
        xmax, ymax = len(board), len(board[0])
        for i in range(xmax):
            for j in range(ymax):
                if board[i][j] == 'R':
                    x, y = i, j
        res = 0
        # left
        for i in range(x, -1, -1):
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                res += 1
                break
        # right
        for i in range(x+1, xmax):
            if board[i][y] == 'B':
                break
            if board[i][y] == 'p':
                res += 1
                break
        # up
        for j in range(y, -1, -1):
            if board[x][j] == 'B':
                break
            if board[x][j] == 'p':
                res += 1
                break
        # down
        for j in range(y+1, ymax):
            if board[x][j] == 'B':
                break
            if board[x][j] == 'p':
                res += 1
                break
        return res
