# With the instruction of http://bookshadow.com/weblog/2015/08/17/leetcode-single-number-iii/.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor = reduce(lambda x, y : x ^ y, nums)
        filterValue = xor & -xor
        a = b = 0
        for i in nums:
            if i & filterValue == 0:
                a ^= i
            else:
                b ^= i
        return [a, b]