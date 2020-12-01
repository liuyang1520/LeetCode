"""
@difficulty: easy
@tags: misc
@notes: use a copy to swap the locations, can save the space with in place swapping.
"""
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        copy = list(s)
        for i in range(len(s)):
            copy[indices[i]] = s[i]
        return "".join(copy)
