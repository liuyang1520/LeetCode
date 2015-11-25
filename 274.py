# Make a dictionary for statistics may save some time to O(n).
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        hIndexValue = 0
        for i in range(len(citations) + 1):
            temp = [j for j in citations if j >= i]
            if len(temp) >= i:
                hIndexValue = i
        return hIndexValue