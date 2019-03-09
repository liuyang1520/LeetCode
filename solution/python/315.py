"""
Fenwich Tree.
[5, 2, 6, 1]
add 1: [1, 0, 0, 0] map to (1, 2, 5, 6) sum of []
add 6: [1, 0, 0, 1] map to (1, 2, 5, 6) sum of [1]
add 2: [1, 1, 0, 1] map to (1, 2, 5, 6) sum of [1]
add 5: [1, 1, 1, 1] map to (1, 2, 5, 6) sum of [1, 1]
Learn from https://www.hrwhisper.me/leetcode-count-of-smaller-numbers-after-self/
"""
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        orderDict = {value: x for x, value in enumerate(sorted(set(nums)))}
        size = len(orderDict)
        fenwickTree = FenwickTree(size)
        res = []
        for i in range(len(nums) - 1, -1, -1):
            fenwickTree.add(orderDict[nums[i]]+1, 1)
            res.append(fenwickTree.sum(orderDict[nums[i]]))
        return res[::-1]
        
class FenwickTree(object):
    def __init__(self, size):
        self.nodes = [0] * (size+1)
        self.size = size
        
    def lowbit(self, x):
        return x & -x
        
    def add(self, x, value):
        while x <= self.size:
            self.nodes[x] += value
            x += self.lowbit(x)
        
    def sum(self, x):
        res = 0
        while x > 0:
            res += self.nodes[x]
            x -= self.lowbit(x)
        return res