# Use string and int for convenience.
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = reduce(lambda x, y: str(x) + str(y), digits)
        num = 1 + int(num)
        return [int(i) for i in str(num)]