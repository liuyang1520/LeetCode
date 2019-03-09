class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashSet = {}


    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hashSet[key] = True
        

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hashSet.pop(key, None)
        

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hashSet:
            return True
        else:
            return False
