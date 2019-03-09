"""
1. Brute-force, got TLE as expected
2. Get how many zeros and ones for each digit for all numbers.
For example:
2, 4, 14
2:  0 0 1 0
4:  0 1 1 0
14: 1 1 1 0
-----------
0s: 2 1 0 3
1:  1 2 3 0
-----------
2 * 1 + 1 * 2 + 0 * 3 + 3 * 0 = 4
"""
class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            for j in nums:
                res += bin(i ^ j).count('1')
        return res / 2


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(32):
            temp = 1 << i
            zeros, ones = 0, 0
            for n in nums:
                if n & temp:
                    ones += 1
                else:
                    zeros += 1
            res += ones * zeros
        return res
