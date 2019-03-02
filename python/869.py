"""
Solution 1: generate all combinations of N, and test whether it is power of 2 one by one.
Solution 2: generate the power of 2 dictionary, then compare the sorted digits with the dictionary
"""
class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        stats = set()
        base = 1
        while base < 1000000000:
            stats.add("".join(sorted(str(base))))
            base *= 2
        return "".join(sorted(str(N))) in stats
