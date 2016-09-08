# Binary indexed tree (Fenwick tree)
# https://www.hrwhisper.me/binary-indexed-tree-fenwick-tree/
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.rangeSum = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            val = nums[i - 1]
            while i <= len(nums):
                self.rangeSum[i] += val
                i += self.__lowBit(i)
        
        
    def __lowBit(self, x):
        return x & -x
        

    def __subSum(self, x):
        res = 0
        while x > 0:
            res += self.rangeSum[x]
            x -= self.__lowBit(x)
        return res


    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.__subSum(j+1) - self.__subSum(i)
        


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)