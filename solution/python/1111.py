"""
@difficulty: easy
@tags: stack
@notes: Use a stack to track the previous left parentheses, can be improved by "(" = 1, ")" = -1 and track the sum value.
"""
class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        stack, res = [], [0] * len(seq)
        for i, s in enumerate(seq):
            if s == "(":
                stack.append(i)
            else:
                temp = stack.pop()
                if len(stack) % 2 == 0:
                    res[i] = 1
                    res[temp] = 1
        return res
