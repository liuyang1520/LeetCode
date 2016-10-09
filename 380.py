"""
Solution 1: Pythonic solution
Solution 2: Use dict and list to record index and value
"""
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomSet = set()

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        contained = True
        if val not in self.randomSet:
            contained = False
            self.randomSet.add(val)
        return not contained

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        contained = False
        if val in self.randomSet:
            contained = True
            self.randomSet.discard(val)
        return contained

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return random.sample(self.randomSet, 1)[0]


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomList = []
        self.randomDict = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.randomDict:
            return False
        self.randomList.append(val)
        self.randomDict[val] = len(self.randomList) - 1
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.randomDict:
            return False
        pos = self.randomDict[val]
        self.randomList[pos], self.randomList[-1] = self.randomList[-1], self.randomList[pos]
        self.randomDict[self.randomList[pos]] = pos
        self.randomDict.pop(val)
        self.randomList.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        return self.randomList[random.randint(0, len(self.randomList) - 1)]