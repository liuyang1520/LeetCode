"""
Use sets to store the pairs and compare one by one
"""
class Solution(obkect):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        if len(words1) != len(words2):
            return False
        similarDict = defaultdict(set)
        for word1, word2 in pairs:
            similarDict[word1].add(word2)
            similarDict[word2].add(word1)
        for i in range(len(words1)):
            if words1[i] == words2[i] or words2[i] in similarDict[words1[i]] or words1[i] in similarDict[words2[i]]:
                continue
            return False
        return True
