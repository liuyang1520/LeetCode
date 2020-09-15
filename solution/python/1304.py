"""
@difficulty: easy
@tags: misc
@notes: to balance the sum, choose a nagetive and position value from the same distance to zero
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            return list(range(1, n // 2 + 1)) + list(range(-1, -int(n // 2) - 1, -1))
        else:
            return list(range(1, n // 2 + 1)) + list(range(-1, -int(n // 2) - 1, -1)) + [0]
