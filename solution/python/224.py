"""
Refer here: https://www.hrwhisper.me/leetcode-math/
Use a stack to process the calculation
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ", "")
        stack = []
        res, temp = 0, 0
        sign = 1
        for i in range(len(s)):
            if s[i] not in "()+-":
                temp = 10*temp + int(s[i])
            if s[i] in "()+-" or i == len(s)-1:
                if s[i] == "(":
                    stack.append([res, sign])
                    res, sign = 0, 1
                elif s[i] == ")":
                    res += temp * sign
                    temp, sign = stack.pop()
                    res = res*sign + temp
                    sign = 1
                else:
                    res += temp * sign
                    sign = 1 if s[i] == "+" else -1
                temp = 0
        return res
                