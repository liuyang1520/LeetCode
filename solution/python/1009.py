"""
@difficulty: easy
@tags: bit
@notes: 1111...11b - N
"""
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        return 2 ** (len(bin(N)) - 2) - N - 1
