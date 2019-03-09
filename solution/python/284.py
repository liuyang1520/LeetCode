# Method 1, re-construct all numbers and re-implement all methods. However, it didn't pass the tests. Don't know why.
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.nums = []
        while iterator.hasNext():
            self.nums.append(iterator.next())
        self.pointer = 0
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nums[self.pointer]

    def next(self):
        """
        :rtype: int
        """
        x = self.nums[self.pointer]
        self.pointer += 1
        return x

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pointer + 1 > len(self.nums) - 1:
            return False
        else:
            return True


# Method 2, Use deep copy to copy the iter object, thus next() won't change the pointer.
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iter = iterator
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        import copy
        return copy.deepcopy(self.iter).next()
        

    def next(self):
        """
        :rtype: int
        """
        return self.iter.next()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.iter.hasNext()


# Method 3, use two variable to indicate the current element and whether next() is called.