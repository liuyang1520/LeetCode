# From LeetCode 287 ---- Find the Duplicate Number

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive),
# prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Note:
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.


# Apply sort method on the array. This solution surely violates the rules 1 and 2. Since sort need extra O(n) spaces 
# if time complexity is below O(n^2)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]


# The following two solutions refer to the blog http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/.

# Use binary search to locate which half has the duplicated numbers.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            center = (left + right) / 2
            count = sum(1 for i in nums if i <= center)
            if count > center:
                right = center - 1
            else:
                left = center + 1
        return left


# The classical Tortoise and Hare algorithm. Refer to the aforementioned Blog.
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        finder = nums[0]
        slow = nums[slow]
        while slow != finder:
            slow = nums[slow]
            finder = nums[finder]
        return finder