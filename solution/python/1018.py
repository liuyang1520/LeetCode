"""
@difficulty: easy
@tags: misc
@notes: subsum = subsum * 2 + new_digit
"""
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        res = []
        subsum = 0
        for i in A:
            subsum = subsum * 2 + i
            if subsum % 5 == 0:
                res.append(True)
            else:
                res.append(False)
        return res
