"""
@difficulty: easy
@tags: misc
@notes: Time complexity O(n^2 * max(word length)).
"""
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for sub in words:
            for word in words:
                if sub != word and sub in word:
                    res.append(sub)
                    break
        return res
