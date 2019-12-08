"""
@difficulty: easy
@tags: misc
@notes: Convert to string to get the digits easily.
"""
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce
        digits = [int(i) for i in str(n)]
        return reduce(lambda x, y: x * y, digits) - reduce(lambda x, y: x + y, digits)
