"""
@difficulty: easy
@tags: misc
@notes: min(clockwise, sum(distance) - clockwise)
"""
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if start > destination:
            destination, start = start, destination
        clockwise = sum(distance[start: destination])
        return min(clockwise, sum(distance) - clockwise)
