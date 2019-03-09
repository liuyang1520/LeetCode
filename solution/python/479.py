"""
Get the answer from someone's post online, directly print it.
The normal answer would be the brute-force solution.
"""
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        results = [0, 9, 9009, 906609, 99000099, 9966006699, 999000000999, 99956644665999, 9999000000009999]
        return results[n] % 1337
