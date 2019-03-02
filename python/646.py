"""
Greedy problem, sort by the second value
"""
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs = sorted(pairs, key = lambda x: x[1])
        lastValue = -float('inf')
        count = 0
        for a, b in pairs:
            if a > lastValue:
                lastValue = b
                count += 1
        return count
