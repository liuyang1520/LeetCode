# Basic DP problem.
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        methods = [0] * n
        methods[0] = 1
        methods[1] = 2
        for i in range(2, n):
            methods[i] = methods[i - 1] + methods[i - 2]
        return methods[n - 1]


# Fibonacci number, Closed-form expression
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt5 = math.sqrt(5)
        return int((((1 + sqrt5) / 2) ** (n + 1) - ((1 - sqrt5) / 2) ** (n + 1)) / sqrt5)