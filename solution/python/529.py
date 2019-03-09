"""
Recursive solution, use a queue to save points that need to go through later.
"""
class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x_max, y_max = len(board)-1, len(board[0])-1
            
        def reveal(x, y):
            if board[x][y] == 'M':
                board[x][y] = 'X'
            elif board[x][y] == 'B' or '1' <= board[x][y] <= '8':
                return
            elif board[x][y] == 'E':
                count, queue = 0, []
                for i in [x-1, x, x+1]:
                    for j in [y-1, y, y+1]:
                        if 0 <= i <= x_max and 0 <= j <= y_max and not (i == x and j == y):
                            if board[i][j] == 'M':
                                count += 1
                            elif board[i][j] == 'E':
                                queue.append([i, j])
                if count > 0:
                    board[x][y] = str(count)
                else:
                    board[x][y] = 'B'
                    for i, j in queue:
                        reveal(i, j)
                        
        reveal(*click)
        return board