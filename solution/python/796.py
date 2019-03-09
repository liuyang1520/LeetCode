"""
Separate the string then reassemble
"""
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(0, len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False
