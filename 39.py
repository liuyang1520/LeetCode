# DFS solution.
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(nums, start, total):
            if total > target or start >= len(candidates):
                return
            if total == target:
                res.append(nums)
            for i in range(0, len(candidates)):
                if start + i < len(candidates):
                    dfs(nums + [candidates[start + i]], start + i, total + candidates[start + i])
                
                
        res = []
        candidates.sort()
        dfs([], 0, 0)
        return res