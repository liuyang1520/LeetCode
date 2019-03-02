"""
Actually:
    r = n % 26
    if r == 0:
        cha = "Z"
    else:
        cha = chr(ord("A") - 1 + r)
    title += cha
can be replaced with:
    title += chr(ord("A") - (n - 1) % 26)
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ""
        while n > 0:
            r = n % 26
            if r == 0:
                cha = "Z"
            else:
                cha = chr(ord("A") - 1 + r)
            title += cha
            n = (n - 1) / 26
        return title[::-1]