"""
Improvements:
1. No need to use set to store visited values, only need to check whether it is -1
2. Value exchanges, `nums[j], j = -1, nums[j]`, no need to use temp
3. Only need to use a size variable to get the size by +1 each time find a new vlue
"""
class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLen = 0

        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            hasNext, j, visited = True, i, set()
            while hasNext:
                if j not in visited:
                    visited.add(j)
                    temp = nums[j]
                    nums[j] = -1
                    j = temp
                else:
                    hasNext = False
                    maxLen = max(maxLen, len(visited))

        return maxLen
