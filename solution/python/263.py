# Divide the num by 2, 3, 5 until there is no factor of 2, 3, 5.
# Note that negative numbers and 0 are not ugly number.
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        flag = True
        while flag:
            flag = False
            if num % 2 == 0:
                num /= 2
                flag = True
            if num % 3 == 0:
                num /= 3
                flag = True
            if num % 5 == 0:
                num /= 5
                flag = True
        if num == 1:
            return True
        else:
            return False