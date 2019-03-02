# Almost same as the previous problem, the difficulties is to dedup.
# 1) sort the candidates;
# 2) if i > pos and candidates[i] == candidates[i - 1], this statement skips a series of duplicate numbers.
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        
        def combinationHelper(subTotal, pos, nums):
            if subTotal == 0:
                res.append(nums)
            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] <= subTotal:
                    combinationHelper(subTotal - candidates[i], i + 1, nums + [candidates[i]])
            
        res = []
        combinationHelper(target, 0, [])
        return res