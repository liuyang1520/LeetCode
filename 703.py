"""
Min-heap with size k
"""
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        import heapq
        self.k = k
        self.heap = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.heap)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.heap) >= self.k:
            heapq.heappushpop(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]
