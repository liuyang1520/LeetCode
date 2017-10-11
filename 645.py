"""
Methods:
1. Python set calculation + sum
2. Summation only
3. x + sum(for i in nums) = y + sum(for i in range)
   x^2 + sum(for i^2 in nums) = y + sum(for i^2 in range)
   now we know x - y and x ^ 2 - y ^ 2, do math calculation
4. Use nagative sign to reuse the nums list for marking a number shows up or not
"""
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = (set(range(1, len(nums) + 1)) - set(nums)).pop()
        dup = missing + (sum(nums) - sum(range(1, len(nums) + 1)))
        return [dup, missing]
