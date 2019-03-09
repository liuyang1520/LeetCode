"""
One iteration, store a pointer pointing to last available position.
"""
class RLEIterator(object):
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = [A[i:i+2] for i in range(0, len(A), 2)]
        self.index = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        value = -1
        if self.index == -1: return value
        for i in range(self.index, len(self.A)):
            if self.A[i][0] < n:
                n -= self.A[i][0]
            else:
                self.A[i][0] -= n
                value = self.A[i][1]
                break
        self.index = i
        if i == len(self.A) - 1 and value == -1:
            self.index = -1
        return value
