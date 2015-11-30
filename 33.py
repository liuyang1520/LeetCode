# Use two binary search, the first one finds the minimum value, the second one searches in the truncated list.
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Find minimum value index.
        left = 0
        right = len(nums) - 1
        miniValue = nums[0]
        mini = -1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
            if nums[mid] <= miniValue:
                mini = mid
                miniValue = nums[mid]
        if target > nums[-1]:
            return self.binarySearch(nums[:mini], target)
        else:
            res = self.binarySearch(nums[mini:], target)
            return [res + mini, res][res == -1]
    
    
    def binarySearch(self, aList, aTarget):
        left = 0
        right = len(aList) - 1
        mid = -1
        while left <= right:
            mid = (left + right) / 2
            if aList[mid] == aTarget:
                break
            elif aList[mid] > aTarget:
                right = mid - 1
            else:
                left = mid + 1
        if mid >= 0 and aList[mid] == aTarget:
            return mid
        else:
            return -1