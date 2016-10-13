"""
Always push the min number we can get, and use 3 pointers to track the current number we already use.
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i = j = k = 0
        while len(res) < n:
            temp = min(res[i] * 2, res[j] * 3, res[k] * 5)
            res.append(temp)
            if res[-1] == res[i] * 2:
                i += 1
            if res[-1] == res[j] * 3:
                j += 1
            if res[-1] == res[k] * 5:
                k += 1
        return res[-1]