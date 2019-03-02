# Recursive solution.
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        return self.combineHelp(range(1, n+1), k)
        
    def combineHelp(self, nums, k):
        if k <= 0 or len(nums) < k:
            return []
        res = []
        for i in range(len(nums)):
            if k == 1:
                res += [[nums[i]]]
            for s in self.combineHelp(nums[i + 1:], k - 1):
                res += [[nums[i]] + s]
        return res


# Learn from the solution in http://chaoren.is-programmer.com/posts/42627.html.
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k <= 0 or n < k:
            return []
        res = []
        temp = [0] * k
        p = 0
        while p >= 0:
            temp[p] += 1
            for i in range(p + 1, k):
                temp[i] = temp[i - 1] + 1
            res += [temp[:]]
            p = k - 1
            while p >= 0 and temp[p] == n - (k - 1 - p):
                p -= 1
        return res