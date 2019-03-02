"""
(num + (1 << 32)) % (1 << 32) gets the two’s complement code for 32 bits int
"""
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        return hex((num + (1 << 32)) % (1 << 32))[2:]

# solution without using hex()
# http://bookshadow.com/weblog/2016/09/25/leetcode-convert-a-number-to-hexadecimal/
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        # return hex((num + (1 << 32)) % (1 << 32))[2:]
        
        # Another solution
        ans = []
        hexs = '0123456789abcdef'
        if num < 0: num += 0x100000000
        while num:
            ans.append(hexs[num % 16])
            num /= 16
        return ''.join(ans[::-1]) if ans else '0'