# Max-heap and min-heap
# https://discuss.leetcode.com/topic/27522/java-python-two-heap-solution-o-log-n-add-o-1-find
import heapq
class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maxHeap = []
        self.minHeap = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if len(self.maxHeap) == len(self.minHeap):
            heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        else:
            heapq.heappush(self.maxHeap, -heapq.heappushpop(self.minHeap, num))
        

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.maxHeap) == len(self.minHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0
        else:
            return self.minHeap[0]