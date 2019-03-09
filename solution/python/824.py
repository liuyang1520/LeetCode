"""
Note the vowel can be lowercase or uppercase
"""
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        res = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        words = S.split(' ')
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels:
                newWord = word + 'ma' + 'a' * (i+1)
            else:
                newWord = word[1:] + word[0] + 'ma' + 'a' * (i+1)
            res.append(newWord)
        return " ".join(res)
