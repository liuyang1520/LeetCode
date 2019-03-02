"""
Use a stack, in which numbers are in ascending order.
"""
class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"
        stack = []
        for i in range(0, len(num)):
            while stack and stack[-1] > num[i] and len(num) - i - 1 + len(stack) >= len(num) - k:
                #if (num[i] == 0 and len(stack) > 1) or num[i] > 0:
                stack.pop()
            if len(stack) < len(num) - k:
                stack.append(num[i])
        return str(int("".join(stack)))