"""
Sort the odd and even chars to combine to a new string as the unique key.
"""
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        formatted = []
        for word in A:
            formatted.append("".join(sorted(word[0::2]) + sorted(word[1::2])))
        return len(set(formatted))
