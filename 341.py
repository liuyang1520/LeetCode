"""
1. use yield and generator in Python;
2. use iterator and stack: http://bookshadow.com/weblog/2016/04/17/leetcode-flatten-nested-list-iterator/
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.generator = self.nextHelper(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.temp
        
    def nextHelper(self, nestedList):
        for i in nestedList:
            if i.isInteger():
                yield i.getInteger()
            else:
                for j in self.nextHelper(i.getList()):
                    yield j
        
    def hasNext(self):
        """
        :rtype: bool
        """
        self.temp = next(self.generator, None)
        if self.temp is not None:
            return True
        else:
            return False
        # or use try except
        # try:
        #     self.temp = self.generator.next()
        # except Exception as e:
        #     return False
        # return True