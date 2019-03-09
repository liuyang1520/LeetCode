# DFS solution
"""
1. If a number is in a cell, ignore it;
2. If it is valid, then go next cell;
3. Test all possiblities until reaching the end.
"""
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def checkValid(x, y):
            for i in range(9):
                if (board[x][y] == board[x][i] and y != i) or (board[x][y] == board[i][y] and x != i):
                    return False
            for i in range(3):
                for j in range(3):
                    x0 = x / 3 * 3 + i
                    y0 = y / 3 * 3 + j
                    if board[x0][y0] == board[x][y] and x0 != x and y0 != y:
                        return False
            return True

        def solveSudokuHelper(x, y):
            if x == 9 and y == 0:
                return True
            if board[x][y] != ".":
                return solveSudokuHelper(x + (y + 1) / 9, (y + 1) % 9)
            for i in range(1, 10):
                board[x][y] = str(i)
                if checkValid(x, y) and solveSudokuHelper(x + (y + 1) / 9, (y + 1) % 9):
                    return True
                board[x][y] = "."
            return False
                
        solveSudokuHelper(0, 0)