# Use two dictionaries to store the a->b and b->a maps.
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapDict = {}
        mapDict2 = {}
        for i in range(len(s)):
            if s[i] not in mapDict:
                mapDict[s[i]] = t[i]
            elif mapDict[s[i]] != t[i]:
                return False
            if t[i] not in mapDict2:
                mapDict2[t[i]] = s[i]
            elif mapDict2[t[i]] != s[i]:
                return False
        return True