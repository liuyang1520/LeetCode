"""
Math problem, only square numbers will last.
"""
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # res = 0
        # for i in range(1, n+1):
        #     count = 0
        #     for j in range(1, i+1):
        #         if i % j == 0:
        #             count += 1
        #     if count % 2:
        #         res += 1
        # return res
        
        return int(n**0.5)