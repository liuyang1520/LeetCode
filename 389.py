"""
Counter
"""
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        scount, tcount = Counter(s), Counter(t)
        return (tcount - scount).keys()[0]