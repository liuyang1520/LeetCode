"""
From end to start:
Find the first non-incremental element, switch it with the start one, then reverse (sorted) the rest.
6,4,5,3,2,1
switch 4, 5
reverse 3,2,1
then 6, 5, 4, 1, 2, 3
Actually the steps can be done in two while loops.
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        maxNum = max(nums)
        for i in range(length-1, -1, -1):
            minMaxNum, jPos = maxNum + 1, -1
            for j in range(i+1, length):
                if nums[j] > nums[i] and nums[j] < minMaxNum:
                    minMaxNum, jPos = nums[j], j
            if minMaxNum != maxNum + 1:
                nums[i], nums[jPos] = nums[jPos], nums[i]
                nums[:] = nums[:i+1] + list(sorted(nums[i+1:]))
                return
        nums[:] = nums[::-1]


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j, k = len(nums)-2, len(nums)-1
        while j >= 0:
            if nums[j] < nums[j+1]: break
            j -= 1
        if j < 0:
            nums.reverse()
            return
        while k > j :
            if nums[k] > nums[j]: break
            k -= 1
        nums[j], nums[k]=nums[k], nums[j]  
        nums[:] = nums[:j+1] + nums[:j:-1]