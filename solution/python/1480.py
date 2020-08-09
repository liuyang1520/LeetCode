"""
@difficulty: easy
@tags: misc
@notes: Python reduce function.
"""
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return reduce(lambda l, x: l + [l[-1] + x], nums, [0])[1:]
