# Should look like 10000, 1000000 in binary expressions.
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        numBin = "{0:b}".format(num)
        if num < 0:
            return False
        if numBin == "1" + "0"*(len(numBin) - 1) and len(numBin) % 2 == 1:
            return True
        return False

# Found another solution https://www.hrwhisper.me/leetcode-power-four/.
return num > 0 and num & (num - 1) == 0 and num & 0x55555555 != 0
# 1. check num > 0
# 2. check 10000000...
# 3. check 1 is before even number of 0s, 0x5555... = 01010101...