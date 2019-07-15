"""
@difficulty: easy
@tags: heap
@notes: Use a heap to manage the max items.
"""
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        import heapq
        heap = map(lambda x: -x, stones)
        heapq.heapify(heap)
        while len(heap) >= 2:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            diff = abs(x - y)
            if diff:
                heapq.heappush(heap, -diff)
        if heap:
            return -heap[0]
        else:
            return 0
