"""
Set to store all words, then sort by length and alpha order
"""
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        wordsSet = set(words)
        sortedWords = sorted(words, key = lambda x: (-len(x), x))
        for word in sortedWords:
            findWord = True
            for i in range(0, len(word)):
                if word[:i+1] not in wordsSet:
                    findWord = False
                    break
            if findWord: return word
        return ""
