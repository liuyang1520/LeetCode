# Binary Search
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        mid = (start + end) / 2
        while guess(mid):
            if guess(mid) > 0: start = mid + 1
            else: end = mid - 1
            mid = (start + end) / 2
        return mid