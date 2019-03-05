"""
@difficulty: easy
@tags: misc
@notes: Counter + intersection, can use Counter api A & B and A.elements() instead.
"""
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        from collections import Counter
        stats = Counter(A[0])
        for word in A[1:]:
            counter = Counter(word)
            for c in stats.keys() + counter.keys():
                stats[c] = min(stats[c], counter[c])
        return sum([val*[i] for i, val in stats.items()], [])
