# DFS problem.
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def combinationHelp(start, count, summation, nums):
            if count > k or summation > n:
                return
            if count == k and summation == n:
                res.append(nums)
                return
            for i in range(start + 1, 10):
                combinationHelp(i, count + 1, summation + i, nums + [i])
        combinationHelp(0, 0, 0, [])
        return res