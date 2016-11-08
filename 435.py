"""
Greedy solution: always pick up the interval with smallest end, and get rid of overlapping intervals.
Improvements: we can only record the number of intervals we need, or we skip wrong intervals instead of deleting those.
http://bookshadow.com/weblog/2016/10/30/leetcode-non-overlapping-intervals/
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key = lambda x: x.end)
        count = 0
        i = 0
        while i < len(intervals):
            j = i + 1
            while j < len(intervals):
                if intervals[j].start < intervals[i].end <= intervals[j].end:
                    intervals.pop(j)
                    count += 1
                else:
                    j += 1
            i += 1
        return count