"""
Use a stack
"""
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for i in S:
            if i == '(':
                stack.append('(')
                continue
            if stack[-1] not in list('()'):
                number = stack.pop()
                stack[-1] = number * 2
            elif stack[-1] == '(':
                stack[-1] = 1
            while len(stack) > 1 and stack[-2] not in list('()'):
                x = stack.pop()
                stack[-1] += x
        return stack[0]
