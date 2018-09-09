"""
Solution 1, TLE, use a set to store words
Solution 2, AC, trie
"""
class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        words.sort(key=lambda x: len(x), reverse=True)
        used = set()
        res = 0
        for word in words:
            overlap = False
            for x in used:
                if x.endswith(word):
                    overlap = True
                    break
            if not overlap:
                used.add(word)
                res += len(word) + 1
        return res


class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        words.sort(key=lambda x: len(x), reverse=True)
        trie = {}
        res = 0
        for word in words:
            overlap = True
            reversedWord = word[::-1]
            trieLookUp = trie
            for l in reversedWord:
                if l in trieLookUp:
                    trieLookUp = trieLookUp[l]
                else:
                    trieLookUp[l] = {}
                    trieLookUp = trieLookUp[l]
                    overlap = False
            if not overlap:
                res += len(word) + 1
        return res
