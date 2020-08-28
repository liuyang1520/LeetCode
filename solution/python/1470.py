"""
@difficulty: easy
@tags: misc
@notes: naive solution. 
"""
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        for i in range(0, n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res
