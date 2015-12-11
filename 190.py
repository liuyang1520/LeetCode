# Int to string in binary, then string to int.
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        nStr = "{:032b}".format(abs(n))[::-1]
        return int(nStr, 2)

# A simple solution.
class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(32):
            ans <<= 1
            ans |= n & 1
            n >>= 1
        return ans