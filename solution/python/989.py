"""
@difficulty: easy
@tags: misc
@notes: Use string is easier and slower.
"""
class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        return list(str(int("".join(map(str, A))) + K))
