# Pythonic solution
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            num = float(s)
            return True
        except:
            return False