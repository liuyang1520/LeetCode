"""
Use a pointer for the index, no need to pop out the element.
"""
class RecentCounter(object):
    def __init__(self):
        self._pings = []
        self._index = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self._pings.append(t)
        while self._index < len(self._pings) and self._pings[self._index] < t - 3000:
            self._index += 1
        return len(self._pings) - self._index
