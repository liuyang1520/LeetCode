"""
@difficulty: easy
@tags: misc
@notes: Counter.
"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        counter = Counter(chars)
        res = 0
        for word in words:
            wcounter = Counter(word)
            canBeFormed = True
            for i in wcounter:
                if i not in counter or counter[i] < wcounter[i]:
                    canBeFormed = False
                    break
            if canBeFormed:
                res += len(word)
        return res
