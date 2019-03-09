"""
Find the smallest common divider (>1) for the counts.
"""
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        from collections import Counter
        counts = sorted(Counter(deck).values())
        if counts[0] == 1:
            return False
        if len(counts) <= 1:
            return True
        for i in range(2, counts[0]+1):
            if counts[0] % i == 0 and counts[1] % i == 0:
                break
        return all(j % i == 0 for j in counts)
