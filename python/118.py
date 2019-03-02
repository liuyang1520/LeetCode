# k th row: c_n^0,...c_n^i,...c_n^n. Alternative solution, use k-1 th row to calculate k th row.
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            res.append([self.c(i, j) for j in range(0, i + 1)])
        return res
        
        
    def c(self, n, k):
        k = min(n - k, k)
        res = 1
        for i in range(n, n-k, -1):
            res = res * i
        for i in range(1, k + 1):
            res /= i
        return res