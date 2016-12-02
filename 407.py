"""
Following the answer here: http://bookshadow.com/weblog/2016/09/25/leetcode-trapping-rain-water-ii/
The idea is to find the max possible height a point has, using BFS.
"""
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0
        
        x_max, y_max = len(heightMap), len(heightMap[0])
        heightMax = [[float('inf')]*y_max for i in range(x_max)]
        queue = []
        for i in range(x_max):
            for j in range(y_max):
                if i == 0 or i == x_max - 1 or j == 0 or j == y_max - 1:
                    queue.append((i, j))
                    heightMax[i][j] = heightMap[i][j]
                    
        while queue:
            x, y = queue.pop(0)
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                xn, yn = x + dx, y + dy
                if 0 <= xn < x_max and 0 <= yn < y_max:
                    maxHeight = max(heightMax[x][y], heightMap[xn][yn])
                    if heightMax[xn][yn] > maxHeight:
                        heightMax[xn][yn] = maxHeight
                        queue.append((xn, yn))
           
        return sum([sum(heightMax[i]) - sum(heightMap[i]) for i in range(x_max)])