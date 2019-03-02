"""
1. OrderedDict
2. Queue (list) + Dictionary
"""
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        import collections
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last = False)
        self.cache[key] = value


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cacheQueue = []
        self.cacheDict = {}

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.cacheDict:
            return -1
        self.cacheQueue.remove(key)
        self.cacheQueue.append(key)
        return self.cacheDict[key]

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        find = self.cacheDict.get(key, "NotFound")
        if find != "NotFound":
            self.cacheQueue.remove(key)
        if find == "NotFound" and len(self.cacheQueue) == self.capacity:
            oldKey = self.cacheQueue.pop(0)
            self.cacheDict.pop(oldKey)
        self.cacheQueue.append(key)
        self.cacheDict[key] = value