# DP solution, however, get Time Limit Exceeded.
def numSquares(n):
        """
        :type n: int
        :rtype: int
        """
        dp = [9999] * (n + 1)
        s = 1
        while s ** 2 <= n:
            dp[s ** 2] = 1
            s += 1
        for i in range(2, n + 1):
            for j in range(1, i / 2 + 1):
                dp[i] = min(dp[i], dp[j] + dp[i - j])
        return dp[n]


# Find a DP solution online. https://leetcode.com/discuss/56993/static-dp-c-12-ms-python-172-ms-ruby-384-ms
class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            # dp += [min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1] same as below.
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


# A very elegant solution, with Lagrange's four-square theorem.
# https://leetcode.com/discuss/56982/o-sqrt-n-in-ruby-and-c
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        while n % 4 == 0:
            n /= 4
        if n % 8 == 7:
            return 4
        i = 0
        while i**2 <= n:
            j = int((n - i**2) ** 0.5)
            if i**2 + j**2 == n: return bool(i) + bool(j)
            i += 1
        return 3