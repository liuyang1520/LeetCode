"""
O(n), one loop
"""
class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        start = end = 0
        res = []
        while end < len(S):
            length = end - start + 1
            if end + 1 == len(S) or S[end + 1] != S[start]:
                if length >= 3:
                    res.append([start, end])
                start = end = end + 1
            else:
                end += 1
        return res
