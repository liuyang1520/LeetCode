"""
Brute force, O(n^3)
"""
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            for j in range(i+1):
                temp = s[j:i+1]
                if temp == temp[::-1]:
                    res += 1
        return res
