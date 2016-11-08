"""
A = [1,3,5,7,9]
dp= [0,0,1,2,3]
sum(dp) is the answer
Use only one variable is fine too
"""
class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        dp = [0] * len(A)
        for i in range(2, len(A)):
            if A[i] + A[i-2] == 2 * A[i-1]:
                dp[i] = dp[i-1] + 1
        return sum(dp)