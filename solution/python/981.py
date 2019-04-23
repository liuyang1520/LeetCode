"""
@difficulty: medium
@tags: binary search
@notes: Hashtable + binary search
"""
class TimeMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.storage = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.storage:
            self.storage[key] = [(value, timestamp)]
        else:
            index = self.binarySearch(self.storage[key], timestamp)
            self.storage[key].insert(index + 1, (value, timestamp))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.storage:
            return ''
        index = self.binarySearch(self.storage[key], timestamp)
        if self.storage[key][index][1] <= timestamp:
            return self.storage[key][index][0]
        return ''
        
    def binarySearch(self, array, timestamp):
        left, right = 0, len(array) - 1
        while left < right:
            mid = (left + right) / 2
            if array[mid][1] <= timestamp:
                left = mid + 1
            else:
                right = mid
        return left - 1
