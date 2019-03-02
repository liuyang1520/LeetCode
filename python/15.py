# a + b + c = 0, use a loop to select a, and find b + c = -a. Use two pointers to find solution in O(n). Total time is O(n^2)
# Need to avoid duplicates, like [-2, -2. 1, 1, 1, 4].
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        res.append([nums[i], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
        return res