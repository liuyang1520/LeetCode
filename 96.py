# First set the root r, than there are f(r - 1) * f(n - r) conditions.
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = {}
        res[0] = 1
        res[1] = 1
        if n == 1:
            return res[1]
        for i in range(2, n + 1):
            res[i] = 0
            for j in range(1, i + 1):
                res[i] += res[i - j] * res[j - 1]
        return res[n]
        