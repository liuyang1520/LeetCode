"""
Brute force, for each digit test whether is divided or not
"""
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for num in range(left, right + 1):
            isSelfDivideNum = True
            for digit in str(num):
                if int(digit) == 0 or num % int(digit) != 0:
                    isSelfDivideNum = False
                    break
            if isSelfDivideNum:
                res.append(num)
        return res
