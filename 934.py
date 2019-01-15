"""
Solution 1:
DFS get the outline of first bridge (i, j).
DFS again get the outline of second bridge (i, j).
Calculate the min-distance by brute-force.
Note, the outline will save time, if we use all the points inside each island, then TLE.
O(A) + O(A) + O(A) = O(A)

Solution 2:
DFS + BFS
"""
class Solution(object):
    def shortestBridge(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        def helper():
            dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            visited = set()
            outline = set()
            def findOne():
                for i in range(len(A)):
                    for j in range(len(A[0])):
                        if A[i][j] == 1:
                            visited.add((i, j))
                            A[i][j] = '#'
                            return i, j
            def dfs(i, j):
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if x >= len(A) or x < 0 or y < 0 or y >= len(A[0]):
                        outline.add((i, j))
                        continue
                    if A[x][y] == 0:
                        outline.add((i, j))
                    if (x, y) not in visited and A[x][y] == 1:
                        A[x][y] = '#'
                        visited.add((x, y))
                        dfs(x, y)
            i, j = findOne()
            dfs(i, j)
            return outline
        
        set1 = helper()
        set2 = helper()
        minDistance = float('inf')
        for x1, y1 in set1:
            for x2, y2 in set2:
                diff = abs(x1 - x2) + abs(y1 - y2) - 1
                minDistance = min(minDistance, diff)
        return minDistance
