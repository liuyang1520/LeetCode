"""
Create a mapping for quick reference and use the list comparison in Python for comparing.
"""
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        mapping = {val: i for i, val in enumerate(order)}
        for i in range(len(words) - 1):
            word1 = [mapping[v] for v in words[i]]
            word2 = [mapping[v] for v in words[i+1]]
            if word1 > word2:
                return False
        return True
