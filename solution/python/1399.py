"""
@difficulty: easy
@tags: misc
@notes: Use hash map to collect the overall information with one iteration.
"""
class Solution:
    def countLargestGroup(self, n: int) -> int:
        stats = {}
        maxSize = 0
        for i in range(1, n+1):
            index = sum(map(int, str(i)))
            if index not in stats:
                stats[index] = 1
            else:
                stats[index] += 1
            if stats[index] > maxSize:
                maxSize = stats[index]
        return list(stats.values()).count(maxSize)
