# Use a list to store the ways from the start to current letter.
# Note that '01' is not a valid case, while '1' is.
# Improvement 1: s[] in numList -> 10 <= int(s[]) <= 26;
# Improvement 2: don't need the dp list actually, only need 2 vars to store previous 2 records.
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        s = "00" + s
        dp = [0] * len(s)
        dp[1] = 1
        numList = [str(i) for i in range(1, 27)]
        for i in range(2, len(s)):
            if int(s[i]) != 0 and (s[i-1: i+1] in numList):
                dp[i] = dp[i - 1] + dp[i - 2]
            elif int(s[i]) == 0 and (s[i-1: i+1] in numList):
                dp[i] = dp[i - 2]
            elif int(s[i]) != 0 and (not (s[i-1: i+1] in numList)):
                dp[i] = dp[i - 1]
        return dp[-1]
