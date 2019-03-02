class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S:
            return 0
        stack = [S[0]]
        for i in range(1, len(S)):
            if stack and stack[-1] == '(' and S[i] == ')':
                stack.pop()
            else:
                stack.append(S[i])
        return len(stack)
