"""
Use counter to get the char distribution, sort the words list before comparing
"""
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter
        words.sort(key = lambda x: len(x))
        counter = Counter([i for i in licensePlate.lower() if i.isalpha()])
        for word in words:
            temp = Counter(word)
            if any(counter[i] > temp[i] for i in counter):
                continue
            return word
