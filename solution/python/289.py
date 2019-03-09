# Use additional O(m*n) to store the values.
# Actually, each cell can store additional information (current and future condition, for example, use two digits 01).
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        boardTemp = [[0] * (n+2)] + [[0] + i[:] + [0] for i in board] + [[0] * (n+2)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                liveTotal = boardTemp[i-1][j] + boardTemp[i+1][j] +\
                            boardTemp[i][j-1] + boardTemp[i-1][j-1] + boardTemp[i+1][j-1] +\
                            boardTemp[i][j+1] + boardTemp[i-1][j+1] + boardTemp[i+1][j+1]
                if boardTemp[i][j] == 1:
                    if liveTotal > 3 or liveTotal < 2:
                        board[i-1][j-1] = 0
                else:
                    if liveTotal == 3:
                        board[i-1][j-1] = 1