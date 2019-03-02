"""
For each word in dictionary, test whether it is a substring of the required one
"""
class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        for word in sorted(d, key=lambda item: (-len(item), item)):
            if self.isSubstring(s, word):
                return word
        return ''

    def isSubstring(self, parentString, subString):
        i = j = 0
        while i < len(parentString) and j < len(subString):
            if parentString[i] == subString[j]:
                i += 1
                j += 1
            else:
                i += 1
            if j == len(subString):
                return True
        return False
