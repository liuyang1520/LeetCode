# Sort the numbers and find the sequence of majority element. Time complexity O(nlogn)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        count = 1
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                count += 1
            else:
                count = 1
            if count > len(nums) / 2:
                return nums[i]


# Alternative solution, Moore's Voting ALgorithm.
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        element = nums[0]
        for i in nums:
            if count == 0:
                element = i
                count = 1
            elif element == i:
                count += 1
            else:
                count -= 1
        return element