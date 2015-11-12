# When i == x: one, two = x, 0;
# When i == x: one, two = 0, x;
# When i == x: one, two = 0, 0.
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = two = 0
        for i in nums:
            one ^= i & ~two
            two ^= i & ~one
        return one