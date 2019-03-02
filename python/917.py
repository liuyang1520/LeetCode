"""
Two pointers from the beginning and the end
"""
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        S = list(S)
        left, right = 0, len(S) - 1
        while left < right:
            if S[left].isalpha() and S[right].isalpha():
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
            elif not S[left].isalpha():
                left += 1
            elif not S[right].isalpha():
                right -= 1
            else:
                left += 1
                right -= 1
        return ''.join(S)
