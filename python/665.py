"""
1. Intuitive solution: check i+1, i th number, and count the disorder pairs
fail on: [3,4,2,3]
2. Add another check whether for the count of larger numbers for current position
fail on: [2,3,3,2,4]
3. Change number according to the situation, and only one chance to change
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        disorderCount = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] < nums[i]:
                disorderCount += 1
            if disorderCount >= 2:
                return False
        return True

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        disorderCount = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                disorderCount += 1
            if disorderCount >= 2:
                return False
            count = 0
            for j in range(i):
                if nums[i] < nums[j]:
                    count += 1
                if count >= 2:
                    return False
        return True

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [-float('inf')] + nums
        i = 1
        changed = 0
        while i < len(nums):
            if nums[i-1] > nums[i]:
                if nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i-2]
                changed += 1
            else:
                i += 1
            if changed >= 2:
                return False
        return True
