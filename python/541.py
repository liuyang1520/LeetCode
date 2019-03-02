"""
Note:
a = [1, 2, 3]
a[::-1] = a[:None:-1] = a[:-len(a)-1:-1] = [3, 2, 1]
However, a[:-1:-1] = []
Because, a[-k] = a[len(a) - k], a[-1] = a[len(a) - 1], 
which is different from range() method.
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        length = len(s)
        sList = list(s)
        for i in range(length / k + 1):
            start, end = i*k, min(i*k+k-1, length)
            if i % 2 == 0:
                sList[start: end+1] = sList[end: start-1: -1] if start > 0 else sList[end: None: -1]
        return "".join(sList)