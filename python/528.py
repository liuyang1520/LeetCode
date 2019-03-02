"""
Example, [1, 2, 3, 4], calculate the probability of the cumulative sums [1, 3, 6, 10].
For a random number in rnage [1, 10], the probability of the index is the length of the interval.
"""
class Solution(object):
    import random
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.segments = []
        subtotal = 0
        for i in w:
            subtotal += i
            self.segments.append(subtotal)

    def pickIndex(self):
        """
        :rtype: int
        """
        value = random.randint(1, self.segments[-1])
        left, right = 0, len(self.segments) - 1
        while left < right:
            mid = (left + right) / 2
            if self.segments[mid] == value:
                return mid
            elif self.segments[mid] < value:
                left = mid + 1
            else:
                right = mid
        return left
