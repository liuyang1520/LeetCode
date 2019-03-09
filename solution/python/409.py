"""
sum = odd - 1, even
aaabbbcc -> aaabbcc
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        counter = Counter(s)
        countOdd, countEven, countMiddle = 0, 0, 0
        for i in counter:
            if counter[i] % 2:
                countMiddle = 1
                countOdd += counter[i]-1
            else:
                countEven += counter[i]
        return countOdd + countEven + countMiddle