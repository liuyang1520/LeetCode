"""
  Pacific ~   ~   ~   ~   ~ 
	   ~  1   2   2   3  (5) *
	   ~  3   2   3  (4) (4) *
	   ~  2   4  (5)  3   1  *
	   ~ (6) (7)  1   4   5  *
	   ~ (5)  1   1   2   4  *
		  *   *   *   *   * Atlantic

[0, 0, 0, 0, 0, 0], 
[0, 1, 2, 2, 3, 5], 
[0, 3, 2, 3, 4, 4], 
[0, 2, 4, 5, 4, 4], 
[0, 6, 7, 5, 4, 5], 
[0, 5, 5, 5, 4, 4]

[4, 4, 4, 4, 5, 0], 
[4, 4, 4, 4, 4, 0], 
[5, 5, 5, 3, 1, 0], 
[6, 7, 1, 4, 5, 0], 
[5, 1, 1, 2, 4, 0], 
[0, 0, 0, 0, 0, 0]

Wrong answer
Next time need to read question carefully, I assume the water is in the center, which is totally wrong.
"""
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """	
        if not matrix:
			return []
			
		x_max, y_max = len(matrix), len(matrix[0])
		dp1 = [[0] * (y_max+1) for i in range(x_max+1)]
		dp2 = [[0] * (y_max+1) for i in range(x_max+1)]
		
		for i in range(1, x_max+1):
			dp1[i][0] = max(dp1[i-1][0], matrix[i-1][0])
		for j in range(1, y_max+1):
			dp1[0][j] = max(dp1[0][j-1], matrix[0][j-1])
		for i in range(x_max-1, -1, -1):
			dp2[i][-1] = max(dp2[i+1][-1], matrix[i][-1])
		for j in range(y_max-1, -1, -1):
			dp2[-1][j] = max(dp2[-1][j+1], matrix[-1][j])
			
		for i in range(1, x_max+1):
			for j in range(1, y_max+1):
				dp1[i][j] = max(min(dp1[i-1][j], dp1[i][j-1]), matrix[i-1][j-1])
				dp2[x_max-i][y_max-j] = max(min(dp2[x_max-i+1][y_max-j], dp2[x_max-i][y_max-j+1]), matrix[x_max-i][y_max-j])

		res = []
		for i in range(0, x_max):
			for j in range(0, y_max):
				if dp1[i+1][j+1] <= matrix[i][j] and dp2[i-1][j-1] <= matrix[i][j]:
					res.append([i, j])
		for i in range(0, x_max+1):
			print dp1[i]
		for i in range(0, x_max+1):
			print dp2[i]
		return res

"""
BFS + Set
"""
class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
            
        x_max, y_max = len(matrix), len(matrix[0])
        pacificSet = set([(0, y) for y in range(y_max)] + [(x, 0) for x in range(x_max)])
        atlanticSet = set([(x_max - 1, y) for y in range(y_max)] + [(x, y_max - 1) for x in range(x_max)])
        
        def bfs(nodeSet):
            moves = [(0, -1), (0, 1), (1, 0), (-1, 0)]
            queue = list(nodeSet)
            while queue:
                x, y = queue.pop(0)
                for dx, dy in moves:
                    xp = x + dx
                    yp = y + dy
                    if 0 <= xp < x_max and 0 <= yp < y_max and matrix[xp][yp] >= matrix[x][y] and (xp, yp) not in nodeSet:
                        queue.append([xp, yp])
                        nodeSet.add((xp, yp))
        bfs(pacificSet)
        bfs(atlanticSet)
        return list(pacificSet & atlanticSet)
