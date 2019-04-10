"""
@difficulty: easy
@tags: misc
@notes: First count all words in B into a single hashmap, then use it to compare words in A one by one.
"""
class Solution(object):
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        stats = Counter()
        for word in B:
            c = Counter(word)
            for key in c:
                stats[key] = max(stats[key], c[key])
        res = []
        for word in A:
            c = Counter(word)
            if all(c[key] >= stats[key] for key in stats):
                res.append(word)
        return res
