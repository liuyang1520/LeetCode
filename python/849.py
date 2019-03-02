"""
Left to right, then right to left, pick whichever smaller value to be the distance for that index
"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        dp = [float('inf')] * len(seats)
        lastIndex = -float('inf')
        # left to right
        for i in range(len(seats)):
            if seats[i]:
                dp[i] = 0
                lastIndex = i
            else:
                dp[i] = min(i - lastIndex, dp[i])
        # right to left
        lastIndex = float('inf')
        for i in range(len(seats)-1, -1, -1):
            if seats[i]:
                dp[i] = 0
                lastIndex = i
            else:
                dp[i] = min(lastIndex - i, dp[i])
        return max(dp)
