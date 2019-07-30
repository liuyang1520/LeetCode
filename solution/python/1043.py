"""
@difficulty: medium
@tags: dp
@notes: dp[i] is the max sum from 1 to i, need to traverse back K items to try the sub-max value for calculating dp[i].
"""
class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0] * (len(A) + 1)
        for i in range(1, len(dp)):
            submax = A[i-1]
            for j in range(i, max(0, i - K), -1):
                submax = max(A[j-1], submax)
                dp[i] = max(dp[j-1] + (i - j + 1) * submax, dp[i])
        return dp[-1]
