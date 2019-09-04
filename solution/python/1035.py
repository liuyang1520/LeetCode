"""
@difficulty: medium
@tags: DP
@notes: Essentially the longest common substring problem.
"""
class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        lenA, lenB = len(A), len(B)
        dp = [[0] * (lenB+1) for i in range(lenA+1)]
        for i in range(1, lenA+1):
            for j in range(1, lenB+1):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + int(A[i-1] == B[j-1]))
        return dp[-1][-1]
