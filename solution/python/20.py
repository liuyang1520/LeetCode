# Use a stack to store the characters, pop each to compare.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        stack = []
        while s:
            a = s[0]
            s = s[1:]
            if a in "([{":
                stack.append(a)
            elif stack:
                b = stack.pop()
                if not ((a == ')' and b == '(') or (a == ']' and b == '[') or (a == '}' and b == '{')):
                    return False
            else:
                return False
        if not stack:
            return True
        else:
            return False