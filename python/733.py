"""
Edge case, when newColor is the same as the old color
"""
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def helper(x, y, color):
            temp = image[x][y]
            image[x][y] = color
            for x_dt, y_dt in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                x_new, y_new = x + x_dt, y + y_dt
                if 0 <= x_new < len(image) and 0 <= y_new < len(image[0]) and image[x_new][y_new] == temp:
                    helper(x_new, y_new, color)

        if image[sr][sc] == newColor:
            return image
        helper(sr, sc, newColor)
        return image
