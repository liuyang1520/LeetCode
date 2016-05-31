# Find answer here http://www.cnblogs.com/TenosDoIt/p/3801621.html.
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def isValid(k, x):
            # Check whether the k-th queen is able to be put in column x.
            for i in range(k):
                if chessboard[i] == x or abs(k - i) == abs(chessboard[i] - x):
                    return False
            return True
                
        def NQueensHelper(queens, result):
            if queens == n:
                # !!! Cannot use res += [result], res variable must be global.
                res.append(result)
                return
            for i in range(n):
                if isValid(queens, i):
                    temp = '.' * n
                    temp = temp[:i] + 'Q' + temp[i + 1:]
                    chessboard[queens] = i
                    NQueensHelper(queens + 1, result + [temp])
        
        res = []
        # No need to pass it into helper, since new records overwrite previous one
        chessboard = [-1 for i in range(n)]
        NQueensHelper(0, [])
        return res