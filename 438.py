"""
Hash map comparison
"""
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        if len(s) < len(p):
            return []
        res = []
        counterp = Counter(p)
        dp = [False] * len(s)
        for i in range(0, len(s)-len(p)+1):
            if i > 0 and (s[i-1] == s[i+len(p)-1] and not dp[i-1]) or (s[i-1] != s[i+len(p)-1] and dp[i-1]):
                continue
            elif (i > 0 and s[i-1] == s[i+len(p)-1] and dp[i-1]) or Counter(s[i: i+len(p)]) == counterp:
                dp[i] = True
                res.append(i)
        return res