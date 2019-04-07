"""
@difficulty: easy
@tags: misc
@notes: Use two pointers to count the left/right parentheses, add to result when equal.
"""
class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        i = 0
        res = []
        while i < len(S):
            j = i
            l, r = 0, 0
            while j < len(S):
                if S[j] == '(':
                    l += 1
                else:
                    r += 1
                    if r == l:
                        res.append(S[i+1:j])
                        i = j + 1
                        break
                j += 1
        return ''.join(res)
