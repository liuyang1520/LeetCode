# Time Limit Exceeded, DFS
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        self.results = 0
        self.nums = sorted(nums)
        self.combinationSumHelper(target)
        return self.results
        
    def combinationSumHelper(self, target):
        for i in self.nums:
            if i < target:
                self.combinationSumHelper(target - i)
            elif i == target:
                self.results += 1
                return
            else:
                return


""" 
Sudo-polynomial solution, DP, like packing problem.
Like Sieve of Eratosthenes algorithm,
target = 5, nums = [1, 1, 2]
dp = [1, 0, 0, 0, 0, 0]
first round: mark all position of nums to 1
dp = [1, 1, 0, 1, 0, 0] (position [0, 1, 2, 3, 4, 5])
iteratively do the above things.
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(target):
            for j in nums:
                if i + j <= target:
                    dp[i + j] += dp[i]
        return dp[target]

