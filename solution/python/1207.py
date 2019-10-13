"""
@difficulty: easy
@tags: misc
@notes: Use counter.
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        counter = Counter(arr)
        return len(counter.values()) == len(set(counter.values()))
