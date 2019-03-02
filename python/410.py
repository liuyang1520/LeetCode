"""
Binary search + greedy

Input:
nums = [7,2,5,10,8]
m = 2

In above case, all subsums should be within [10, 32], namely [max(nums), sum(nums)].
We can run a binary search on the possibilities of subsums, and a greedy algorith to test whether a subsum value is valid.
For example, mid = (10 + 32) / 2 = 21, since 7 + 2 + 5 < 21 and 7 + 2 + 5 + 10 > 21, so the first split must be [7, 2, 5].
And [10, 8] is valid, so the split strategy is valid. We can try some number smaller than 21.

The tricky part of this problem is testing whether a subsum value is valid can be done in linear time with a greedy solution.
"""
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def isValidSplit(subTotal):
            countSplit, subSum = 1, 0
            for i in range(len(nums)):
                if subSum + nums[i] > subTotal:
                    countSplit += 1
                    if countSplit > m:
                        return False
                    subSum = nums[i]
                else:
                    subSum += nums[i]
            return True 
            
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = (left + right) / 2
            if isValidSplit(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left