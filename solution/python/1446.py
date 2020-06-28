"""
@difficulty: easy
@tags: misc
@notes: One iteration, use a pointer to compare against the previous element.
"""
class Solution:
    def maxPower(self, s: str) -> int:
        prev, curLength, maxLength = s[0], 1, 1
        for i in range(1, len(s)):
            if s[i] == prev:
                curLength += 1
                maxLength = max(curLength, maxLength)
            else:
                curLength = 1
                prev = s[i]
        return maxLength
