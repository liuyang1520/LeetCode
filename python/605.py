"""
Add '0' to left and right, count how many 0s in each segment continuously, then do the math.
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        import math
        flowerbedStr = '0' + "".join(map(lambda x: str(x), flowerbed)) + '0'
        flowerbedCount = map(lambda x: max(0, math.ceil((len(x) - 2)/2.0)), flowerbedStr.split('1'))
        return sum(flowerbedCount) >= n
