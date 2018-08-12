class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        counter = Counter((A + " " + B).split(' '))
        return [i for i, j in counter.items() if j == 1]
