# DP: from bottom right to top left
# health[i][j] = max(1, min(health[i+1][j], health[i][j+1]) - dungeon[i][j])
# http://www.davex.pw/2016/01/21/LeetCode-Dungeon-Game/
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        width, length = len(dungeon), len(dungeon[0])
        health = [[1000000]*(length + 1) for i in range(width + 1)]
        health[width][length] = health[width][length-1] = health[width-1][length] = 1
        for i in range(width - 1, -1, -1):
            for j in range(length - 1, -1, -1):
                health[i][j] = max(1, min(health[i+1][j], health[i][j+1]) - dungeon[i][j])
        return health[0][0]