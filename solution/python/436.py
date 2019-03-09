"""
1. brute-force, TLE as expected;
2. store start values and do binary search.
"""
class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        res = []
        for inter in intervals:
            minStart = (float('inf'), -1)
            for j in range(len(intervals)):
                if intervals[j].start >= inter.end and intervals[j].start < minStart[0]:
                    minStart = (intervals[j].start, j)
            res.append(minStart[1])
        return res


class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        res = []
        startList = sorted((inter.start, index) for index, inter in enumerate(intervals))
        for inter in intervals:
            end = inter.end
            left, right = 0, len(startList)-1
            while left <= right:
                mid = left + (right - left) / 2
                if startList[mid][0] >= end:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(startList):
                res.append(-1)
            else:
                res.append(startList[left][1])
        return res