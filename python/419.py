"""
DFS
or:
check (x > 0 and board[x-1][y] == "X") or (y > 0 and board[x][y-1] == "X"), since battleships have separators
"""
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "X":
                    count += 1
                    if (x > 0 and board[x-1][y] == "X") or (y > 0 and board[x][y-1] == "X"):
                        count -= 1
        return count