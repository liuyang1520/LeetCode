"""
xxx00 -> xxx0
xxx01 -> xxx00
xxx10 -> xxx1
xxx11 -> xx(x+1)00
When it ends with 11 (n % 4 == 3), +1 always better than -1
"""
class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        repDict = {1: 0, 2: 1, 3: 2, 4: 2}
        stillRunning = True
        res = 0
        while stillRunning:
            if n in repDict:
                return res + repDict[n]
            if n % 2 == 0:
                n /= 2
            elif n % 4 == 1:
                n -= 1
            elif n % 4 == 3:
                n += 1
            res += 1