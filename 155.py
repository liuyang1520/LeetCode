# Use another stack to track the min value of current minStack
# Example:
# minStack: 2, 4, 6, 1, 4, 1
# traceMin: 2,  ,  , 1,  , 1
# Note: 1 must be append twice, or the min value will lost.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minStack = []
        self.traceMin = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minStack.append(x)
        if len(self.traceMin):
            if x <= self.traceMin[-1]:
                self.traceMin.append(x)
        else:
            self.traceMin.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        if self.minStack[-1] == self.traceMin[-1]:
            self.traceMin.pop()
        self.minStack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.traceMin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()