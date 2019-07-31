"""
@difficulty: easy
@tags: misc
@notes: Or apply the GCD algorithm to string, however, slicing string will be linear time.
"""
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        from fractions import gcd
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        str1Len, str2Len = len(str1), len(str2)
        maxLength = gcd(str1Len, str2Len)
        for i in range(maxLength, 0, -1):
            if str1Len % i == 0 and str2Len % i == 0:
                substring = str1[:i]
                if self.isDividable(str1, substring) and self.isDividable(str2, substring):
                    return substring
        return ""
        
    def isDividable(self, string, substring):
        i = 0
        while i < len(string):
            for j in range(0, len(substring)):
                if string[i+j] != substring[j]:
                    return False
            i = i + j + 1
        return True
