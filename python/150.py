"""
Use a stack to store the values.
Note: Python calculate the wrong result for negative divisions, 6/-144 = -1 instead of 0, need to override this.
Or: "/": (lambda x, y: int(float(x)/y))
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        from operator import add, sub, mul
        stack = []
        res = 0
        operatorDict = {"+": add, "-": sub, "*": mul, "/": (lambda x, y: -(abs(x)/abs(y)) if x * y < 0 else x / y)}
        for i in tokens:
            if i not in operatorDict:
                stack.append(int(i))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operatorDict[i](a, b))
        return stack.pop()