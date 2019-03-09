"""
Brute-force solution.
A stack O(n) solution is here:
https://discuss.leetcode.com/topic/77916/java-10-lines-linear-time-complexity-o-n-with-explanation
"""
class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for target in findNums:
            findTarget, valid = False, False
            for j in range(len(nums)):
                if target == nums[j]:
                    findTarget = True
                if findTarget and nums[j] > target:
                    res.append(nums[j])
                    valid = True
                    break
            if not valid:
                res.append(-1)
        return res