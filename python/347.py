"""
Pythonic solution, exactly the use case of collections.Counter
Or use heap to keep length k records
"""
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        numsCounter = collections.Counter(nums)
        return [i[0] for i in numsCounter.most_common(k)]


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections, heapq
        numsCounter = collections.Counter(nums)
        heap = []
        for value in numsCounter:
            if len(heap) < k:
                heapq.heappush(heap, [numsCounter[value], value])
            else:
                if heap[0][0] < numsCounter[value]:
                    heapq.heappushpop(heap, [numsCounter[value], value])
        return [i[1] for i in heap]