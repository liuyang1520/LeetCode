# Binary search.
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        left = 0
        right = len(citations) - 1
        hIndexValue = 0
        while left <= right:
            mid = (left + right) / 2
            interval = len(citations) - mid
            if citations[mid] >= interval:
                hIndexValue = max(hIndexValue, interval)
                right = mid - 1
            else:
                left = mid + 1
        return hIndexValue