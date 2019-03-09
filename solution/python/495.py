"""
Calculate the time slots without poison.
"""
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        disconnect = 0
        for i in range(len(timeSeries)-1):
            disconnect += max(0, timeSeries[i+1] - timeSeries[i] - duration)
        return timeSeries[-1] - timeSeries[0] - disconnect + duration