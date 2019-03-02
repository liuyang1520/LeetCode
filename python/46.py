# Pick up a number to put in the left, the get f(n-1) and attack to the right side.
# A better way to achieve permutation is, pick up the first number x, get f(n-1) for rest numbers, insert x in n
# positions, repeat.
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 2:
            return [nums]
        res = []
        for i in range(len(nums)):
            res += [[nums[i]] + j for j in self.permute(nums[:i] + nums[i+1:])]
        return res