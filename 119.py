# Refer to 118.
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return []
        return [self.c(rowIndex, j) for j in range(0, rowIndex + 1)]
        
        
    def c(self, n, k):
        k = min(n - k, k)
        res = 1
        for i in range(n, n-k, -1):
            res = res * i
        for i in range(1, k + 1):
            res /= i
        return res