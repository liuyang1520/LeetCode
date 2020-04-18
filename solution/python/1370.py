"""
@difficulty: easy
@tags: misc
@notes: Counter the string then sort all chars.
"""
class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        counter = Counter(s)
        chars = sorted(counter.keys())
        iteratedLength = 0
        length = len(chars)
        res = []
        while iteratedLength < length:
            for c in chars + chars[::-1]:
                if counter[c] > 0:
                    res.append(c)
                    counter[c] -= 1
                    if counter[c] == 0:
                        iteratedLength += 1
        return "".join(res)
