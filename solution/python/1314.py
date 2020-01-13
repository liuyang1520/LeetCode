"""
@difficulty: medium
@tags: range sum
@notes: Brute-force with O(mnK^2) got TLE. Need to use previous calculation result for improving performance like below.
Another method is to calculate range sum subsum[i][j], sum x: 0->i, y: 0->j,
then res[i][j] = res[i+k][j+k] - res[i-k][j+k] - res[i+k][j-k] + res[i-k][j-k].
"""
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        res = [[0] * len(mat[0]) for i in range(len(mat))]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                subsum = 0
                if j >= 1:
                    subsum += res[i][j-1]
                    for dx in range(-K, K+1):
                        x = i + dx
                        y = j - 1 - K
                        if 0 <= x < len(mat) and 0 <= y < len(mat[0]):
                            subsum -= mat[x][y]
                        y = j + K
                        if 0 <= x < len(mat) and 0 <= y < len(mat[0]):
                            subsum += mat[x][y]
                else:
                    for dx in range(-K, K+1):
                        for dy in range(-K, K+1):
                            x, y = i + dx, j + dy
                            if 0 <= x < len(mat) and 0 <= y < len(mat[0]):
                                subsum += mat[x][y]
                res[i][j] = subsum
        return res
