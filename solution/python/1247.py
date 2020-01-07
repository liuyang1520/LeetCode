"""
@difficulty: medium
@tags: misc
@notes: "xx" "yy" only needs 1 swap, greedy solution.
"""
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        temp = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                temp.append({"x": 0, "y": 1}[s1[i]])
        if len(temp) % 2: return -1
        countx = temp.count(0)
        if countx % 2:
            return len(temp) // 2 + 1
        else:
            return len(temp) // 2
