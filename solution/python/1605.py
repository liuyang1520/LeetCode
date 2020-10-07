"""
@difficulty: medium
@tags: misc
@notes: greedily find the global smallest value then update row and columns, this can be further simplified to just greedily finding the min value in each i, j pair.
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        xmax, ymax = len(rowSum), len(colSum)
        res = [[0] * ymax for i in range(xmax)]
        hasNext = True
        while hasNext:
            hasNext = False
            xminValue, xminIndex = float("inf"), -1
            for i in range(xmax):
                if rowSum[i] > 0 and rowSum[i] < xminValue:
                    xminValue, xminIndex = rowSum[i], i
                    hasNext = True
            yminValue, yminIndex = float("inf"), -1
            for j in range(ymax):
                if colSum[j] > 0 and colSum[j] < yminValue:
                    yminValue, yminIndex = colSum[j], j
                    hasNext = True
            if hasNext:
                minValue = min(xminValue, yminValue)
                res[xminIndex][yminIndex] = minValue
                rowSum[xminIndex] -= minValue
                colSum[yminIndex] -= minValue
        return res
