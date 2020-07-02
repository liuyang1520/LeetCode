"""
@difficulty: medium
@tags: misc
@notes: Intuitive solution.
"""
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        cur = 0
        for i in range(1, n + 1):
            if n % i == 0:
                cur += 1
            if cur == k:
                return i
        return -1
