# O(nlogn), sort
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        num = 1
        for i in range(0, len(nums)):
            if nums[i] > 0 and nums[i] == num:
                num += 1
            elif nums[i] > 0 and (i > 0 and nums[i] > nums[i - 1]):
                return num
        return num


# http://bookshadow.com/weblog/2015/09/14/leetcode-first-missing-positive/
"""
The key is to put nums[i] in nums[i] - 1 position.
For example:
[-1, 1, 4, 2, 5]
[1, -1, 4, 2, 5]
[1, -1, 2, 4, 5] -> [1, 2, -1, 4, 5]
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            while nums[i] > 0 and nums[i] <= n and \
              nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1