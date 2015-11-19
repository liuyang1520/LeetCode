# Make two pointers move from left and right side, always keep the longer line (guarantee the new value is larger).
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            area = max(area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area