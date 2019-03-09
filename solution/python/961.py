"""
Set to check duplicates
"""
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        trace = set()
        for i in A:
            if i in trace:
                return i
            else:
                trace.add(i)
