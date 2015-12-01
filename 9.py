# Use extra space, reverse the int (str) and compare it to itself.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xStr = str(x)
        return xStr == xStr[::-1]


# Use constant extra space solution. Compare the leftmost and rightmost digits, iteratively.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div *= 10
        while x:
            if x / div != x % 10:
                return False
            x = (x % div) / 10
            div /= 100
        return True