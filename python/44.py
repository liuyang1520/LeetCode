"""
2D-DP, gets TLE
dp[i][j] means s[:i] p[:j] matches or not
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(0, len(s) + 1):
            for j in range(1, len(p) + 1):
                if i > 0 and (p[j-1] == s[i-1] or p[j-1] == "?"):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    for k in range(i+1):
                        if dp[k][j-1]:
                            dp[i][j] = True
                            break
        return dp[-1][-1]


"""
Actually, the dp formulation can be simplified,
if p[j] = "*": dp[i][j] = dp[i-1][j] or dp[i][j-1]
No need to look up all dp[k][j - 1]
For example: abc, a*
dp[3][2] = dp[2][2] (True, since dp[1][2] is True) or dp[3][1] (False)
Also, need to cut the edge cases, len(p) - p.count("*") > len(s), which is obviously unachievable.
Note: the 2d dp can be replaced with two 1d dp arraies, since we only need dp[i-1][j-1]
"""
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if len(p) - p.count("*") > len(s):
            return False
        dp = [[False] * (len(p) + 1) for i in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(0, len(s) + 1):
            for j in range(1, len(p) + 1):
                if i > 0 and (p[j-1] == s[i-1] or p[j-1] == "?"):
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]