# Python way solution.
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x = s.split()
        if x:
            return len(x[-1])
        else:
            return 0