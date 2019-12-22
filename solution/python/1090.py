"""
@difficulty: medium
@tags: misc
@notes: Solution 1 use heap to lock the number of items for speeding; Solution 2, sorting all entries at first, count down the use_limit with label.
"""
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        import heapq
        stats = {}
        for i in range(len(values)):
            v, l = values[i], labels[i]
            if l not in stats:
                stats[l] = [v]
            elif len(stats[l]) < use_limit:
                stats[l].append(v)
            else:
                heapq.heapify(stats[l])
                heapq.heappushpop(stats[l], v)
        res = [0] * num_wanted
        heapq.heapify(res)
        for nums in stats.values():
            for num in nums:
                heapq.heappushpop(res, num)
        return sum(res)
