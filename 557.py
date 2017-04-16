"""
Split, reverse, join

or use double reverse:
"abc def" -> "def abc" -> "cba fed"
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(map(lambda x: x[::-1], s.split(" ")))