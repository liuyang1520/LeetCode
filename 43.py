# Pythonic solution
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))


# Simulating the multiplication process
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = num1[::-1]
        num2 = num2[::-1]
        multiDigits = [0] * (len(num1) + len(num2))
        for i in range(len(num1)):
            for j in range(len(num2)):
                multiDigits[i+j] += int(num1[i]) * int(num2[j])
        for i in range(len(multiDigits) - 1):
            temp = multiDigits[i]
            multiDigits[i] = temp % 10
            multiDigits[i + 1] += temp / 10
        res = "".join([str(i) for i in multiDigits])[::-1].lstrip("0")
        return "0" if not res else res