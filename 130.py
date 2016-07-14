"""
For 4 edges, find all "O" and convert them to "T" with DFS;
Iterate all values and convert "O" to "X", "T" to "O".
"""
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or 2 >= len(board) > 0 or 2 >= len(board[0]) > 0:
            return
        
        lenx = len(board)
        leny = len(board[0])
        def bfs(x, y):
            queue = [(x, y)]
            while queue:
                px, py = queue.pop()
                board[px][py] = "T"
                for i, j in [(px-1, py), (px+1, py), (px, py-1), (px, py+1)]:
                    if 0 <= i <= lenx - 1 and 0 <= j <= leny - 1 and board[i][j] == "O":
                        queue.append((i, j))
        
        for j in range(leny):
            if board[0][j] == "O":
                bfs(0, j)
            if board[lenx - 1][j] == "O":
                bfs(lenx - 1, j)
        for i in range(lenx):
            if board[i][0] == "O":
                bfs(i, 0)
            if board[i][leny - 1] == "O":
                bfs(i, leny - 1)
                
        for i in range(lenx):
            for j in range(leny):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"