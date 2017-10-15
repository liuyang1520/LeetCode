"""
O(n) solution, go through the string once, prevCount stores the count for 0/1s of last group, currentCount stores current group
"""
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prevCount, currentCount = 0, 1
        res = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                prevCount = currentCount
                currentCount = 1
            else:
                currentCount += 1
            if prevCount and currentCount <= prevCount:
                res += 1
        return res
