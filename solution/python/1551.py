"""
@difficulty: medium
@tags: math
@notes: sum then calculate
"""
class Solution:
    def minOperations(self, n: int) -> int:
        array = range(1, n * 2 + 1, 2)
        return sum([abs(n - i) for i in array]) // 2
