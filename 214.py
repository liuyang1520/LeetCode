# Find solution online http://bookshadow.com/weblog/2015/05/22/leetcode-shortest-palindrome/.
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        newS = s + "$" + s[::-1]
        kmpList = [0] * len(newS)
        for i in range(1, len(newS)):
            j = kmpList[i - 1]
            while j > 0 and newS[i] != newS[j]:
                j = kmpList[j - 1]
            # kmpList[i] = kmpList[j] + (newS[i] == newS[j])
            if newS[i] == newS[j]:
                kmpList[i] = j + 1
            else:
                kmpList[i] = j
        return s[len(s)-1:kmpList[-1]-1:-1] + s