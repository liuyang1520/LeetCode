# Pythonic solution
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.lstrip().rstrip()
        s = s.split()
        return " ".join(reversed(s))