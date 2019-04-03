"""
@difficulty: medium
@tags: DFS, graph
@notes: From the four edges, run DFS to set the connected 1s to 0s, then count the 1s in whole graph.
"""
class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(x, y):
            if A[x][y] == 0: return
            A[x][y] = 0
            for dx, dy in dirs:
                xnew, ynew = x + dx, y + dy
                if 0 <= xnew < len(A) and 0 <= ynew < len(A[0]):
                    dfs(xnew, ynew)

        # run dfs on all edge nodes
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i == 0 or i == len(A) - 1 or j == 0 or j == len(A[0]) - 1:
                    dfs(i, j)
        # count other 1s
        count = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    count += 1
        return count
