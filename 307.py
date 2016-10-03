"""
Fenwick tree
"""
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        self.rangeSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            val = nums[i - 1]
            while i <= len(nums):
                self.rangeSum[i] += val
                i += self._lowBit(i)
                
    def _lowBit(self, x):
        return x & -x
        
    def _subSum(self, x):
        res = 0
        while x > 0:
            res += self.rangeSum[x]
            x -= self._lowBit(x)
        return res
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        pos = i
        i = i + 1
        while i <= len(self.nums):
            self.rangeSum[i] += val - self.nums[pos]
            i += self._lowBit(i)
        self.nums[pos] = val
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._subSum(j+1) - self._subSum(i)


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.update(1, 10)
# numArray.sumRange(1, 2)