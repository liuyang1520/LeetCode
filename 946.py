"""
@difficulty: medium
@tags: stack
@notes: Simulate the stack push and pop process, pops whenever matches.
"""
class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        i, j, stack = 0, 0, []
        while j < len(popped):
            if stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                continue
            if i == len(pushed):
                return False
            if pushed[i] != popped[j]:
                stack.append(pushed[i])
            else:
                j += 1
            i += 1
        if not stack:
            return True
