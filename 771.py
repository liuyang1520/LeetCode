"""
Simple question, use counter or `in` operation
"""
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        from collections import Counter
        jewels, stones = set(J), Counter(S)
        count = 0
        for key in jewels:
            count += stones[key]
        return count
