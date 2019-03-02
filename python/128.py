# Use a dictionary to store the nums, search time in average O(1).
# Pick up one number and find the longest sequence before and after it, mark those as read.
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numsDic = {}
        for i in nums:
            numsDic[i] = True
        longestNum = 0
        for i in nums:
            longest = 1
            numsDic[i] = False
            minus = plus = 1
            while i - minus in numsDic and numsDic[i - minus]:
                numsDic[i - minus] = False
                longest += 1
                minus += 1
            while i + plus in numsDic and numsDic[i + plus]:
                numsDic[i + plus] = False
                longest += 1
                plus += 1
            if longest > longestNum: longestNum = longest
        return longestNum