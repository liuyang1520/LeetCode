"""
Check each bit and reverse it by replacing chars in string.
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(bin(num)[2:].replace('0', 'x').replace('1', '0').replace('x', '1'), base = 2)