"""
Many cases are the same, actually there is need to use set, see
https://discuss.leetcode.com/topic/102033/java-o-1/2
"""
class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if m == 1 else 4
        results = set()
        if m > 5:
            if m % 2:
                m = 5
            else:
                m = 6
        for a in range(2):
            for b in range(m+1-a):
                for c in range(m+1-a-b):
                    d = m+1 - a - b - c
                    results.add(((a + b) % 2, (a + c) % 2, d % 2))
        return len(results)
