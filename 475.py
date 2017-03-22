"""
Sort + binary search
"""
class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        minRadius = 0
        for house in houses:
            temp = float('inf')
            
            left, right = 0, len(heaters) - 1
            while left < right:
                mid = (left + right) / 2
                if house < heaters[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            closeSet = [max(0, left-1), min(len(heaters)-1, left+1), left]
            for k in closeSet:
                temp = min(abs(house - heaters[k]), temp)

            minRadius = max(temp, minRadius)
        return minRadius