# Two pointer from start to end
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length_t = len(t)
        pos = 0
        findLetter = True
        for letter in s:
            findLetter = False
            while pos < length_t:
                if letter == t[pos]:
                    findLetter = True
                    pos += 1
                    break
                pos += 1
        if not findLetter:
            return False
        else:
            return True