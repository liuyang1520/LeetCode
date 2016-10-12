"""
Addition
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        num1, num2 = num1[::-1], num2[::-1]
        res = ""
        for i in range(len(num2)):
            if i < len(num1):
                temp = int(num1[i]) + int(num2[i]) + carry
            else:
                temp = int(num2[i]) + carry
            carry = temp / 10
            res += str(temp % 10)
        if carry: res += "1"
        return res[::-1]