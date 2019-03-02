"""
1. Brute-force, compare each pair, O(n^2)
2. Map the time into dictionary, and compare the distance between them, O(n)
"""
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minDiff = float('inf')
        for i in range(len(timePoints)):
            for j in range(i+1, len(timePoints)):
                time_diff = self.timeDiff(timePoints[i], timePoints[j])
                if time_diff == 0:
                    return time_diff
                minDiff = min(minDiff, time_diff)
        return minDiff

    def timeDiff(self, time1, time2):
        time1_hour, time1_minute = map(int, time1.split(':'))
        time2_hour, time2_minute = map(int, time2.split(':'))
        time1_to_min = 60 * time1_hour + time1_minute
        time2_to_min = 60 * time2_hour + time2_minute
        time_diff = abs(time1_to_min - time2_to_min)
        return min(time_diff, 1440 - time_diff)
