"""
1. brute-froce, TLE
2. temp = temp + sum(A) - length * A[length - i]
"""
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        res = -float('INF')
        length = len(A)
        for i in range(length):
            temp = 0
            for j in range(length):
                temp += A[(i+j) % length] * j
            res = max(temp, res)
        return res


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        length = len(A)
        temp = sum(A[i] * i for i in range(length))
        res = temp
        sumA = sum(A)
        for i in range(1, length):
            temp = temp + sumA - length * A[length - i]
            res = max(temp, res)
        return res