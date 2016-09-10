# Get whether a char is repeated in first round
# Check the first char not repeated in second round
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        appearedTwice = {}
        for i in s:
            if i not in appearedTwice:
                appearedTwice[i] = False
            else:
                appearedTwice[i] = True
        for i in range(len(s)):
            if not appearedTwice[s[i]]: return i
        return -1