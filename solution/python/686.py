"""
Actually, (repeating A) when A is longer than B, then we can stop. As adding more will be useless.
"""
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if B in A: return 1
        times = max(2, len(B) / len(A))
        for i in range(times, times * 2 + 1):
            if B in (A * i):
                return i
        return -1
