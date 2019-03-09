"""
See https://leetcode.com/problems/beautiful-array/discuss/186679/C%2B%2BJavaPython-Odd-%2B-Even-Pattern-O(N)
"""
class Solution(object):
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        res = [1]
        while len(res) < N:
            res = [i*2 for i in res] + [i*2-1 for i in res]
        return [i for i in res if i <= N]
