"""
divide then combine
"""
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "0"
        neg = True if num < 0 else False
        digits = []
        num = abs(num)
        while num:
            digits.append(str(num % 7))
            num = num / 7
        negSign = "-" if neg else ""
        return negSign + "".join(digits)[::-1]