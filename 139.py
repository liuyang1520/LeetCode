# DP solution
# dp[i] = dp[j] + s[j:i] is in wordDict, for j in letters before i
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
        return dp[-1]


# DFS, Time Limit Exceed
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s:
            return True
        for i in wordDict:
            if s.startswith(i) and self.wordBreak(s[len(i):], wordDict):
                return True
        return False