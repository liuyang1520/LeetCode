"""
dictionary {set()} + list
"""
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.randomList = []
        self.randomDict = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.randomList.append(val)
        findVal = False
        if val not in self.randomDict:
            findVal = True
            self.randomDict[val] = set([len(self.randomList) - 1])
        else:
            self.randomDict[val].add(len(self.randomList) - 1)
        return findVal
            

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.randomDict:
            return False
        if len(self.randomList) - 1 in self.randomDict[val]:
            oriPos = len(self.randomList) - 1
            self.randomDict[val].discard(len(self.randomList) - 1)
        else:
            oriPos = self.randomDict[val].pop()
        lastElement = self.randomList[-1]
        if lastElement != val:
            self.randomList[-1], self.randomList[oriPos] = val, lastElement
            self.randomDict[lastElement].discard(len(self.randomList) - 1)
            self.randomDict[lastElement].add(oriPos)
        if not self.randomDict[val]:
            self.randomDict.pop(val)
        self.randomList.pop()
        return True
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        import random
        return self.randomList[random.randint(0, len(self.randomList) - 1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()