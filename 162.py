# O(n) solution.
class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1 or nums[1] < nums[0]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums) - 1
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i


# Found a binary search solution online http://bookshadow.com/weblog/2014/12/06/leetcode-find-peak-element/.
mid = (start + end) / 2
if num[mid] < num[mid - 1]: # there must be a peak value in the first half
    return self.search(num, start, mid - 1)
if num[mid] < num[mid + 1]: # there must be a peak value in the second half
    return self.search(num, mid + 1, end)
return mid