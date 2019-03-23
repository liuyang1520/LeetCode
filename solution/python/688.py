"""
@difficulty: medium
@tags: DP
@notes: Think it reversely, the last step K is coming from K-1, by summing the probabilities.
"""
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[1] * N for i in range(N)]
        ds = sum([[[i, j], [j, i]] for i in [-2, 2] for j in [-1, 1]], [])
        for _ in range(K):
            temp = [[1] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    sub = 0
                    for dx, dy in ds:
                        if 0 <= i + dx < N and 0 <= j + dy < N:
                            sub += dp[i+dx][j+dy] / 8.0
                    temp[i][j] = sub
            dp = temp
        return dp[r][c]
