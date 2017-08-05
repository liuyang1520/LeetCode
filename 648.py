"""
1. get the set of words, in which longer duplicate words are reset as '#', special character
2. use two for loop to update the sentence

Use a Trie structure would be a better solution
"""
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        for i in range(len(dict)):
            for j in range(i+1, len(dict)):
                if dict[j].startswith(dict[i]):
                    dict[j] = '#'
        wordSet = set(dict)
        sentenceList = sentence.split()
        for i in range(len(sentenceList)):
            for word in wordSet:
                if sentenceList[i].startswith(word):
                    sentenceList[i] = word
        return " ".join(sentenceList)
