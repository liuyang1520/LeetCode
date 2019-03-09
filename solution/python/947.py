"""
@difficulty: medium
@tags: union-find, graph
@notes: Union-Find
"""
class DS(object):
    def __init__(self, count):
        self.parents = range(count)
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, x, y):
        self.parents[self.find(x)] = self.find(y)

class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        ds = DS(20000)
        for i, j in stones:
            ds.union(i, j + 10000)
        return len(stones) - len(set(ds.find(i) for i, j in stones))
