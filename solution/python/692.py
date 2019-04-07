"""
@difficulty: medium
@tags: misc
@notes: count and sort, or use a heap
"""
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter
        counter = Counter(words)
        items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:k]
        return map(lambda x: x[0], items)
