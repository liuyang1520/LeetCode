"""
1. Get the counter of s
Iterate values in s:
2. if value in stack, counter--
3. if value not in stack, if value < stack.top and counter(stack.top) > 0, pop stack
repeat 3
stack.append(value); counter--
"""
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        import collections
        counter = collections.Counter(s)
        stack = []
        for i in s:
            counter[i] -= 1
            if i not in stack:
                while stack and stack[-1] > i and counter[stack[-1]]:
                    stack.pop()
                stack.append(i)
        return "".join(stack)