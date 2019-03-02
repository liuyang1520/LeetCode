# Refer to problem 15.
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dif = 100000
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                left = i + 1
                right = len(nums) - 1
                while left < right:
                    temp = nums[i] + nums[left] + nums[right] - target
                    if temp == 0:
                        return target
                    elif temp < 0:
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    else:
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    if abs(temp) < abs(dif):
                        dif = temp
        return target + dif