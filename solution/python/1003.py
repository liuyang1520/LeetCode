"""
@difficulty: medium
@tags: string, stack
@notes: Solution 1 wrong answer, failed on "aabbcc", Solution 2 correct using a stack
"""
class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        counts = {'a': 0, 'b': 0, 'c': 0}
        for i in S:
            counts[i] += 1
            if counts['a'] < counts['b'] or counts['a'] < counts['c'] or counts['b'] < counts['c']:
                return False
        if counts['a'] == counts['b'] == counts['c']:
            return True
        return False


class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for s in S:
            stack.append(s)
            flag = True
            while len(stack) >= 3 and flag:
                if stack[len(stack)-3:] == list('abc'):
                    stack = stack[:len(stack)-3]
                else:
                    flag = False
        return len(stack) == 0
