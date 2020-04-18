"""
@difficulty: easy
@tags: misc
@notes: Use counter.
"""
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        counter = Counter(arr)
        maxLuckyInt = -1
        for i in counter:
            if i == counter[i] and i > maxLuckyInt:
                maxLuckyInt = i
        return maxLuckyInt
