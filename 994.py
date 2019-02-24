"""
BFS
"""
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        mins = 0
        xmax, ymax = len(grid), len(grid[0])
        total = sum(1 for i in range(xmax) for j in range(ymax) if grid[i][j] == 1)
        queue = [[i, j] for i in range(xmax) for j in range(ymax) if grid[i][j] == 2]
        while queue:
            temp = []
            for x, y in queue:
                for i, j in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                    xnew, ynew = min(max(x + i, 0), xmax-1), min(max(y + j, 0), ymax-1)
                    if grid[xnew][ynew] == 1:
                        temp.append([xnew, ynew])
                        grid[xnew][ynew] = 2
                        total -= 1
            queue = temp
            if temp:
                mins += 1
        if total:
            return -1
        return mins
