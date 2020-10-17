"""
@difficulty: easy
@tags: misc
@notes: use set to store the visited values
"""
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = {(x, y)}
        dirMap = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}
        for i in path:
            xd, yd = dirMap[i]
            x, y = x + xd, y + yd
            if (x, y) in visited:
                return True
            else:
                visited.add((x, y))
        return False
