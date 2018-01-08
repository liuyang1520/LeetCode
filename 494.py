"""
DFS, TLE
Find subsums and store in list, TLE
Find subsums and store in dict, AC
"""
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.total = 0
        self.target = S
        self.dfs(0, nums)
        return self.total

    def dfs(self, subsum, nums):
        if not nums:
            return
        if len(nums) == 1 and ((subsum + nums[-1] == self.target) or (subsum - nums[-1] == self.target)):
            if nums[-1] == 0:
                self.total += 1
            self.total += 1
            return
        self.dfs(subsum + nums[0], nums[1:])
        self.dfs(subsum - nums[0], nums[1:])

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        sums = [0]
        for i in nums:
            temp = []
            for j in sums:
                temp.append(j + i)
                temp.append(j - i)
            sums = temp
        return sums.count(S)

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        from collections import Counter
        sums = Counter([0])
        for i in nums:
            temp = Counter()
            for j in sums.keys():
                temp[j + i] += sums[j]
                temp[j - i] += sums[j]
            sums = temp
        return sums[S]
