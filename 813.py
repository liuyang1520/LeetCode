"""
DP solution, dp[i][k] is the max score sum A[0-i] with k groups.
Solution 1 is slow as it calculates sum averages every time.
Solution 2 precalculates the accumulated sums array, and then sums[j] - sums[i] + A[i] is the sum of i-j.
"""
class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        # dp[i][k] is the max score sum A[0-i] with k groups
        def sumAve(i, j):
            return sum(A[i: j+1]) / float(j - i + 1)
        dp = [[0]*(K+1) for i in range(len(A))]
        for k in range(1, K+1):
            dp[0][k] = A[0]
        for i in range(1, len(A)):
            for k in range(1, K+1):
                for j in range(0, i):
                    if k == 1:
                        dp[i][k] = max(dp[j][k-1] + sumAve(0, i), dp[i][k])
                    else:
                        dp[i][k] = max(dp[j][k-1] + sumAve(j+1, i), dp[i][k])
        return dp[-1][-1]

class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        # dp[i][k] is the max score sum A[0-i] with k groups
        sums = [A[0]]
        for i in range(1, len(A)):
            sums.append(sums[i-1] + A[i])
        def sumAve(i, j):
            return (sums[j] - sums[i] + A[i]) / float(j - i + 1)
        dp = [[0]*(K+1) for i in range(len(A))]
        for k in range(1, K+1):
            dp[0][k] = A[0]
        for i in range(1, len(A)):
            for k in range(1, K+1):
                for j in range(0, i):
                    if k == 1:
                        dp[i][k] = max(dp[j][k-1] + sumAve(0, i), dp[i][k])
                    else:
                        dp[i][k] = max(dp[j][k-1] + sumAve(j+1, i), dp[i][k])
        return dp[-1][-1]
