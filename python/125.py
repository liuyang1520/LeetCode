"""
Pythonic solution
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        for i in s:
            if i.isalnum():
                res.append(i.lower())
        return True if list(reversed(res)) == res else False