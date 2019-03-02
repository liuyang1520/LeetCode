"""
Straight forward solution, O(9 * n * m)
"""
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        neighbors = [
            [i, j] for i in [-1, 0, 1] for j in [-1, 0 , 1]
        ]
        result = [[0]*len(M[0]) for i in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                total, subsum = 0, 0
                for offset in neighbors:
                    xnew, ynew = i + offset[0], j + offset[1]
                    if 0 <= xnew < len(M) and 0 <= ynew < len(M[0]):
                        total += 1
                        subsum += M[xnew][ynew]
                result[i][j] = subsum / total
        return result
