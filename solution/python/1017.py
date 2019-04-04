"""
@difficulty: medium
@tags: math, bit
@notes: Keep dividing by -2 just like 2, take care the divisible condition.
"""
class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        # example N = 6
        # 6 / -2 = -3 --- 0
        # -3 / -2 = 2 --- 1
        # 2 / -2 = -1 --- 0
        # -1 / -2 = 1 --- 1
        # 1 / -2 = 0 --- 1
        # 11010 = 16 - 8 - 2 = 6
        # example N = 3
        # 3 / -2 = -1 --- 1
        # -1 / -2 = 1 --- 1
        # 1 / -2 = 0 --- 1
        # 111 = 4 - 2 + 1 = 3
        if N == 0: return '0'
        res = []
        while N:
            if N % -2 == 0:
                div = N / -2
            else:
                div = N / -2 + 1
            rem = N - div * (-2)
            res.append(rem)
            N = div
        return ''.join(map(str, res[::-1]))
