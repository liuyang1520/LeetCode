# Upper case and lower case!!!
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left = 0
        right = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        while left < right:
            while (s[left] not in vowels) and left < right:
                left += 1
            while (s[right] not in vowels) and left < right:
                right -= 1
            if (s[left] in vowels) and (s[right] in vowels):
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
        return "".join(s)