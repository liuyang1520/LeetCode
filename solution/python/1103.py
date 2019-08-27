"""
@difficulty: easy
@tags: misc
@notes: Simulate the distribution process.
"""
class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        dist = [0] * num_people
        cur, pos = 1, 0
        while candies > 0:
            if candies > cur:
                dist[pos] += cur
                candies -= cur
            else:
                dist[pos] += candies
                candies = 0
            cur += 1
            pos = (pos + 1) % num_people
        return dist
