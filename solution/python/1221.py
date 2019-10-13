"""
@difficulty: easy
@tags: misc
@notes: One iteration.
"""
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = {"L": 0, "R": 0}
        res = 0
        for i in s:
            count[i] += 1
            if count["L"] == count["R"]:
                res += 1
                count = {"L": 0, "R": 0}
        return res
