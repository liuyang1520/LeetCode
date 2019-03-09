"""
1. sort on all elements
2. max-heap of size k
3. binary search on diagonal values
"""
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        size = len(matrix)
        matrixFlat = []
        for i in range(size):
            for j in range(size):
                matrixFlat.append(matrix[i][j])
        matrixFlat.sort()
        return matrixFlat[k-1]