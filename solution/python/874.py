"""
Need to calculate the MAX distance, not the destination distance
"""
class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        directions = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
        mapping = {-1: 1, -2: -1}
        obstacles = set(map(tuple, obstacles))
        x, y, d = 0, 0, 0
        res = 0
        for i in commands:
            if i < 0:
                d = (d + mapping[i]) % 4
            else:
                xd, yd = directions[d]
                for j in range(i):
                    if (x+xd, y+yd) in obstacles:
                        break
                    else:
                        x += xd
                        y += yd
                    res = max(res, x ** 2 + y ** 2)
        return res
