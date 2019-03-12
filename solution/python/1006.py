"""
@difficulty: easy
@tags: misc, math
@note: Brute-Force solution.
Other solutions including eval and math, see https://leetcode.com/problems/clumsy-factorial/discuss/252250/Python-1-line-Cheat.
"""
class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        if N <= 3:
            return [0, 1, 2, 6][N]
        for i in range(N, 3, -4):
            if i == N:
                res += i * (i-1) / (i-2) + (i-3)
            else:
                res += -int(i * (i-1) / (i-2)) + (i-3)
        i = i % 4
        if i == 3:
            return res - 6
        if i == 2:
            return res - 2
        if i == 1:
            return res - 1
        return res
