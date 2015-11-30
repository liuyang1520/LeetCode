# dp[i] is the longest increasing subsequence value, ending with nums[i]. Time complexity O(n^2).
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)


# Use a list to store the sorted longest increasing subsequence, update the value x:
# 1) if x is larger than the right-most value, append it.
# 2) if x is in the middle of the list, replace the slightly larger value with x.
# O(nlogn)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        longestList = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > longestList[-1]:
                longestList.append(nums[i])
            else:
                left = 0
                right = len(longestList)
                while left <= right:
                    mid = (left + right) / 2
                    if longestList[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid - 1
                longestList[left] = nums[i]
        return len(longestList)