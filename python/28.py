# This naive solution is pretty slow.
# Don't know why find "" in "" should return 0.
# Doubt that KMP may have better performance.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nlen = len(needle)
        hlen = len(haystack)
        if nlen == 0 and hlen == 0:
            return 0
        if nlen > hlen:
            return -1
        for i in range(hlen):
            if haystack[i: i+nlen] == needle:
                return i
        return -1
        
# Python's method is very quick.
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
