"""
Modify the ops numbers in place.
Need to convert the string to integer.
"""
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        i = 0
        while i < len(ops):
            if ops[i] == 'D':
                ops[i] = ops[i-1] * 2
            elif ops[i] == '+':
                ops[i] = ops[i-1] + ops[i-2]
            elif ops[i] == 'C':
                ops.pop(i)
                ops.pop(i-1)
                i = i - 2
            else:
                ops[i] = int(ops[i])
            i += 1
        return sum(ops)
