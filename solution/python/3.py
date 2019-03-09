"""
	dp[i] is the longest substring length including current character.
	If s[i] is not detected in previous substring, +1;
	else, find the location and update dp.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [1] * len(s)
        for i in range(1, len(s)):
            temp = s[i-dp[i-1]:i]
            if s[i] not in temp:
                dp[i] = dp[i-1] + 1
            else:
                for j in range(len(temp) - 1, -1, -1):
                    if temp[j] == s[i]:
                        dp[i] = dp[i - 1] - j
                        break
        return max(dp)