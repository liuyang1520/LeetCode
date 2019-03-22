"""
@difficulty: easy
@tags: misc
@notes: Brute-force is O(n^2), only need to group the times then go through those.
"""
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        stats = [0] * 60
        for i in time:
            stats[i % 60] += 1
        res = 0
        for i in range(1, 30):
            res += stats[i] * stats[60 - i]
        res += stats[0] * (stats[0] - 1) / 2
        res += stats[30] * (stats[30] - 1) / 2
        return res
