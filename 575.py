"""
len(set(candies)) is better
"""
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        from collections import Counter

        counter = Counter(candies)
        if len(counter) <= len(candies) / 2:
            return len(counter)
        return len(candies) / 2
