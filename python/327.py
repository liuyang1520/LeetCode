"""
https://www.hrwhisper.me/leetcode-count-of-range-sum/
For every sum[j], need to find the number of records satisfying: lower + sum[i – 1] ≤ sum[j] ≤ upper + sum[i – 1]
The tricky part of this solution is that it calculates result the same time it adds thing to Fenwick Tree.
Since j >= i, for j = n, it has the total(j); for j = n-1, it has the total(j) and total(j-1)

####
Sample input:
[-2,5,-1]
-2
2

####
Sample output
sums:
[-5, -3, -2, -1, 0, 2, 3, 4, 5]
i = 2
[0, 0, 0, 0, 0, 0, 1, 0, 1, 0] (tree)
i = 3
[0, 0, 0, 0, 0, 0, 1, 1, 2, 0] (tree)
i = -2
[0, 0, 0, 1, 1, 0, 1, 1, 3, 0] (tree)
"""
class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        sums = [lower - 1, upper]
        subTotal = 0
        for i in nums:
            subTotal += i
            sums += [subTotal, subTotal + lower - 1, subTotal + upper]
            
        index = {}
        for i, j in enumerate(sorted(set(sums))):
            index[j] = i + 1
            
        fenwickTree = FenwickTree(len(index))
        res = 0
        for i in range(len(nums) - 1, -1, -1):
            fenwickTree.add(index[subTotal], 1)
            subTotal -= nums[i]
            res += fenwickTree.sum(index[subTotal + upper]) - fenwickTree.sum(index[subTotal + lower - 1])
        return res
        
        
# Fenwick Tree, or Binary Indexed Tree
class FenwickTree(object):
    def __init__(self, length):
        self.treeList = [0] * (length + 1)
        self.length = length
        
    def __lowBit(self, val):
        return val & -val
        
    def add(self, pos, val):
        while pos <= self.length:
            self.treeList[pos] += val
            pos += self.__lowBit(pos)
            
    def sum(self, pos):
        res = 0
        while pos > 0:
            res += self.treeList[pos]
            pos -= self.__lowBit(pos)
        return res