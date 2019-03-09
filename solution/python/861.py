"""
Greedy solution, first toggle row to make leftmost column to be all 1s, then tollge column to make as many as 1s for each column.
"""
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        for i in range(len(A)):
            if not A[i][0]:
                A[i] = [j ^ 1 for j in A[i]]
        for i in range(len(A[0])):
            col = [A[j][i] for j in range(len(A))]
            if col.count(0) * 2 > len(A):
                for j in range(len(A)):
                    A[j][i] ^= 1
        total = 0
        for i in range(len(A)):
            total += int("".join(map(str, A[i])), 2)
        return total
