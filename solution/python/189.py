# Other solutions: http://bookshadow.com/weblog/2015/02/24/leetcode-rotate-array/
# Note that the condition that n is divided by k.
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        temp = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = temp[i]