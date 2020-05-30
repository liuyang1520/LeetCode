"""
@difficulty: easy
@tags: misc
@notes: O(n), only need to get the left ones/zeros count
"""
class Solution:
    def maxScore(self, s: str) -> int:
        zeros = s.count("0")
        ones = len(s) - zeros
        leftZeros, leftOnes = 0, 0
        res = 0
        for i in range(0, len(s) - 1):
            if s[i] == "0":
                leftZeros += 1
            else:
                leftOnes += 1
            rightOnes = ones - leftOnes
            res = max(res, leftZeros + rightOnes)
        return res
