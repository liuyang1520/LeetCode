"""
1, 10, 100, 101, ...
Go to x * 10 branch at first, then go to x + 1, if x % 10 < 9
Recursive solution gets TLE.
"""
class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def lexicalOrderHelper(x):
            res.append(x)
            if x * 10 <= n:
                lexicalOrderHelper(x * 10)
            if x + 1 <= n and x % 10 < 9:
                lexicalOrderHelper(x + 1)
        res = []
        lexicalOrderHelper(1)
        return res


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        stack = [1]
        while stack:
            num = stack.pop()
            res.append(num)
            if num + 1 <= n and num % 10 < 9:
                stack.append(num + 1)
            if num * 10 <= n:
                stack.append(num * 10)
        return res