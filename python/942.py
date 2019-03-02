"""
Use the smallest or largest number, then others will form a N-1 problem, and so on.
"""
class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res, low, up = [], 0, len(S)
        for i in S:
            if i == 'I':
                res.append(low)
                low += 1
            else:
                res.append(up)
                up -= 1
        return res + [low]
