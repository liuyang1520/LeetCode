"""
Use binary search to figure out where to insert.
Need to handle the merge: [1,3], [5,7], [11,20], insert 4.
"""
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._interval = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        start = self.searchStart(val)
        if self._interval and ((start == len(self._interval) and val > self._interval[start-1].end + 1) or (start == 0 and self._interval[start].start - 1 > val)):
            self._interval.insert(start, Interval(val, val))
            return
        s, e = val, val
        if start > 0 and self._interval[start-1].end + 1 >= val:
            start -= 1
        while start < len(self._interval) and e + 1 >= self._interval[start].start:
            e = max(self._interval[start].end, e)
            s = min(self._interval[start].start, s)
            self._interval.pop(start)
        self._interval.insert(start, Interval(s, e))
    
    def searchStart(self, target):
        left, right = 0, len(self._interval) - 1
        while left <= right:
            mid = (left + right) / 2
            if self._interval[mid].start > target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        return self._interval


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()