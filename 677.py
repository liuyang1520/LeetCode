"""
The best answer should be using a Trie.
However, the dataset is small, so a dictionary works here.
"""
class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pairDict = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.pairDict[key] = val

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        total = 0
        for key in self.pairDict.keys():
            if key.startswith(prefix):
                total += self.pairDict[key]
        return total
