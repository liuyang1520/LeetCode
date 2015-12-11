class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in board:
            for j in i:
                if not ('1' <= j <= '9' or j == "."):
                    return False
        for row in board:
            row = [i for i in row if i != "."]
            if len(set(row)) != len(row):
                return False
        for j in range(len(board[0])):
            col = [i[j] for i in board if i[j] != "."]
            if len(set(col)) != len(col):
                return False
        block = [[] for i in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if 0 <= i <= 2 and 0 <= j <= 2:
                        block[0].append(int(board[i][j]))
                    elif 0 <= i <= 2 and 3 <= j <= 5:
                        block[1].append(int(board[i][j]))
                    elif 0 <= i <= 2 and 6 <= j <= 8:
                        block[2].append(int(board[i][j]))
                    elif 3 <= i <= 5 and 0 <= j <= 2:
                        block[3].append(int(board[i][j]))
                    elif 3 <= i <= 5 and 3 <= j <= 5:
                        block[4].append(int(board[i][j]))
                    elif 3 <= i <= 5 and 6 <= j <= 8:
                        block[5].append(int(board[i][j]))
                    elif 6 <= i <= 8 and 0 <= j <= 2:
                        block[6].append(int(board[i][j]))
                    elif 6 <= i <= 8 and 3 <= j <= 5:
                        block[7].append(int(board[i][j]))
                    elif 6 <= i <= 8 and 6 <= j <= 8:
                        block[8].append(int(board[i][j]))
        for i in block:
            if len(set(i)) != len(i):
                return False
        return True