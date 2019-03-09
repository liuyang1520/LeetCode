"""
Always choose the leftmost digit to swap with the rightmost largest value.
Use a hash to speed up the compare process.
"""
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        from collections import Counter
        numStr = str(num)
        counter = Counter(numStr)
        for i, val in enumerate(numStr):
            counter[val] -= 1
            for x in range(9, 0, -1):
                if str(x) > val and counter[str(x)] > 0:
                    index = len(numStr) - 1 - numStr[::-1].find(str(x))
                    return int(numStr[:i] + numStr[index] + numStr[i+1:index] + numStr[i] + numStr[index+1:])
        return num
