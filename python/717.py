"""
1. DP
2. Pointer starts from left, move 2 when it is 1, move 1 when it is 0. Judge based on the location of the pointer finally.
3. Regex
"""
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        if bits[-1]: return False
        if len(bits) == 1: return not bool(bits[0])
        if len(bits) >= 2 and bits[-2:] == [0, 0]: return True
        dp = [False] * len(bits)
        dp[0] = False if bits[0] else True
        for i in range(1, len(bits)):
            if (bits[i] and bits[i-1] and not dp[i-1]) or (not bits[i]):
                dp[i] = True
        if dp[-2]:
            return True
        return False
