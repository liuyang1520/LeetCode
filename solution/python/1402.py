"""
@difficulty: hard
@tags: misc
@notes: Sort the array, then find the min index that sum(satisfaction[i:]) >= 0, that is the break point.
"""
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        subSum = 0
        for i in range(len(satisfaction) - 1, -1, -1):
            subSum += satisfaction[i]
            if subSum < 0:
                i += 1
                break
        res = 0
        for index, value in enumerate(satisfaction[i:]):
            res += (index + 1) * value
        return res
