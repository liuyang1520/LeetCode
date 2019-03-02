# Reverse the string for convenience.
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        reverseS = s[::-1]
        col = 0
        for i in range(len(s)):
            col += (ord(reverseS[i]) - ord("A") + 1) * (26 ** i)
        return col