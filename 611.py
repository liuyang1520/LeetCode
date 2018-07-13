"""
Sort the numbers, then find the number smaller than the first two edges.
k doesn't need to go back when j changes
"""
class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        k = 2
        count = 0
        for i in range(length):
            k = i + 2
            if not nums[i]: continue
            for j in range(i+1, length):
                while k < length and nums[i] + nums[j] > nums[k]:
                    k += 1
                count += k - j - 1
        return count
