"""
BFS,
when searching whether a new word is in the list or not, construct a new one and test whether it is in the set.
"""
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [(beginWord, 1)]
        while queue:
            lastWord, length = queue.pop(0)
            for i in range(len(lastWord)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    newWord = lastWord[:i] + j + lastWord[i+1:]
                    if newWord == endWord:
                        return length + 1
                    if newWord != lastWord and newWord in wordList:
                        queue.append((newWord, length + 1))
                        wordList.remove(newWord)
        return 0