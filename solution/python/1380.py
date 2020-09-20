"""
@difficulty: easy
@tags: misc
@notes: brute-force solution
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        xmax, ymax = len(matrix), len(matrix[0])
        res = []
        for i in range(xmax):
            minVal = min(matrix[i])
            indexOfMinVal = matrix[i].index(minVal) # all elements are distinct
            if minVal == max([matrix[j][indexOfMinVal] for j in range(xmax)]):
                res.append(minVal)
        return res
