# Divide and conquer. Split string to a non-frequent character.
class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        sdict = dict()
        for i in s:
            sdict[i] = sdict.get(i, 0) + 1
        for i in sdict.keys():
            if sdict[i] < k:
                return max(self.longestSubstring(j, k) for j in s.split(i))
        return len(s)
