# Sort the list, then insert into it like this:
# b3, b6, b2, b5, b1, b4
# Another solution here: https://leetcode.com/discuss/77133/o-n-o-1-after-median-virtual-indexing
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        newNums = sorted(nums)
        for i in range(1, len(nums), 2):
            nums[i] = newNums.pop()
        for i in range(0, len(nums), 2):
            nums[i] = newNums.pop()