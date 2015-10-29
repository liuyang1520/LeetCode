# The question doesn't permit division, however, I didn't think up alternative solutions.
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = reduce(lambda x, y: x * y, nums)
        if total != 0:
            return map(lambda t: total / t, nums)
        else:
            if nums.count(0) > 1:
                return [0] * len(nums)
            else:
                return [reduce(lambda x, y: x * y, [j for j in nums if j != 0]) if i == 0 else 0 for i in nums]


# Inspired by http://bookshadow.com/weblog/2015/07/16/leetcode-product-array-except-self/. Use two iterations to calculate each value from both two sides.
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        left = right = 1
        for i in range(len(nums) - 1):
            left *= nums[i]
            result[i + 1] *= left
        for i in range(len(nums) - 1, 0, -1):
            right *= nums[i]
            result[i - 1] *= right
        return result