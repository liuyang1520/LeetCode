"""
1. Brute-force, O(n^2), TLE
2. https://leetcode.com/problems/contiguous-array/discuss/99655/Python-O(n)-Solution-with-Visual-Explanation
"""
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        for i in range(len(nums) - 1):
            count = [0, 0]
            count[nums[i]] += 1
            for j in range(i+1, len(nums)):
                count[nums[j]] += 1
                if count[0] == count[1] and count[0]*2 > longest:
                    longest = count[0]*2
        return longest
        
        
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = subsum = 0
        stats = {0: -1}
        for i in range(len(nums)):
            subsum += [-1, 1][nums[i]]
            if subsum in stats:
                res = max(res, i - stats[subsum])
            else:
                stats[subsum] = i
        return res
