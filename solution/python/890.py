"""
Need to map twice to see any violations
"""
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def testMapping(wordA, wordB):
            mapping = {}
            for i in range(len(wordA)):
                if wordA[i] not in mapping:
                    mapping[wordA[i]] = wordB[i]
                else:
                    if mapping[wordA[i]] != wordB[i]:
                        return False
            return True

        res = []
        for word in words:
            if testMapping(word, pattern) and testMapping(pattern, word):
                res.append(word)
        return res
