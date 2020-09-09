"""
@difficulty: medium
@tags: Fenwick tree
@notes: this solution is brute-froce with O(N^2) time complexity, using a Fenwick tree to simulate the position move operation can improve the performance to O(nlgn)
"""
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        init = list(range(1, m + 1))
        res = []
        for i in queries:
            index = init.index(i)
            res.append(index)
            init = [i] + init[:index] + init[index+1:]
        return res
