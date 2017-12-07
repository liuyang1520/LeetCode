"""
Find the first index and reverse track the index should change
"""
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = str(N)
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                j = i
                while j-1 >= 0 and int(s[j-1]) == int(s[i]):
                    j -= 1
                return int(s[:j] + str(int(s[j])-1) + "9" * (len(s)-j-1))
        return N
