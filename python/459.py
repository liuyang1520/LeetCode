"""
For each i, if the string doesn't match. temp refreshes to the new string.
"""
class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type str: str
        :rtype: bool
        """
        length = len(str)
        temp = str[0]
        i = 1
        while i < length:
            plus = len(temp)
            if i+plus == length and str[i: i+plus] == temp:
                return True
            if i+plus < length and str[i: i+plus] != temp:
                temp = str[: i+1]
                i += 1
            else:
                i += plus
        return False