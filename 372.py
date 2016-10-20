"""
currentDigitMod is the mod for current digit:
225, [a % 1337, a^10 % 1337, a^10^10 & 1337]
res is the mod for the total
"""
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        res = 1
        currentDigitMod = a
        for i in reversed(b):
            res = (res * currentDigitMod ** i) % 1337
            currentDigitMod = (currentDigitMod ** 10) % 1337
        return res