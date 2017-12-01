"""
1. Use a set track and pass the set as a parameter so it forks during DFS
2. Use a global set to track and revert it when doesn't find a match in a branch during DFS
3. Change the original board to '#' when it is visited, and revert it back when dismatch during DFS
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(x, y, chars, track):
            if not chars:
                return True
            if len(chars) == 1:
                return board[x][y] == chars[0]
            if board[x][y] == chars[0]:
                temp = set(track)
                temp.add((x, y))
                for x_dt, y_dt in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x_new, y_new = x + x_dt, y + y_dt
                    if (0 <= x_new < len(board) and
                        0 <= y_new < len(board[0]) and
                        (x_new, y_new) not in temp and
                        helper(x_new, y_new, chars[1:], temp)):
                        return True
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, word, set()):
                    return True
        return False


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(x, y, chars):
            if not chars:
                return True
            if len(chars) == 1:
                return board[x][y] == chars[0]
            if board[x][y] == chars[0]:
                visited.add((x, y))
                for x_dt, y_dt in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x_new, y_new = x + x_dt, y + y_dt
                    if (0 <= x_new < len(board) and
                        0 <= y_new < len(board[0]) and
                        (x_new, y_new) not in visited and
                        helper(x_new, y_new, chars[1:])):
                        return True
                visited.discard((x, y))
            return False

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited = set()
                if helper(i, j, word):
                    return True
        return False


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def helper(x, y, chars):
            if not chars:
                return True
            if len(chars) == 1:
                return board[x][y] == chars[0]
            if board[x][y] == chars[0]:
                temp = chars[0]
                board[x][y] = '#'
                for x_dt, y_dt in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    x_new, y_new = x + x_dt, y + y_dt
                    if (0 <= x_new < len(board) and
                        0 <= y_new < len(board[0]) and
                        board[x_new][y_new] != '#' and
                        helper(x_new, y_new, chars[1:])):
                        return True
                board[x][y] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if helper(i, j, word):
                    return True
        return False
