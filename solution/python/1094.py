"""
@difficulty: medium
@tags: interval
@notes: Improvement 1, only need to record the start, end position for number change, iterate once.
Improvement 2, no need to store 1001 values, only store the number diff then sort by start time.
"""
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        stats = [0] * 1001
        for c, s, e in trips:
            for i in range(s, e):
                stats[i] += c
        if max(stats) > capacity:
            return False
        return True
