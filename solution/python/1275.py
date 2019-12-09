"""
@difficulty: easy
@tags: misc
@notes: Intuitive solution.
"""
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [["N"] * 3 for i in range(3)]
        for index in range(len(moves)):
            turn = ["X", "O"][index % 2]
            i, j = moves[index]
            board[i][j] = turn
        def winner(array):
            if array == ["X"] * 3:
                return "A"
            if array == ["O"] * 3:
                return "B"
        for i in range(3):
            if winner(board[i]):
                return winner(board[i])
        for j in range(3):
            res = winner([board[i][j] for i in range(3)])
            if res:
                return res
        res = winner([board[0][0], board[1][1], board[2][2]])
        if res:
            return res
        res = winner([board[2][0], board[1][1], board[0][2]])
        if res:
            return res
        if len(moves) == 9:
            return "Draw"
        return "Pending"
