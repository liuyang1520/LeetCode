"""
@difficulty: easy
@tags: misc
@notes: Only need to check whether the robot moves or it changes direction after running one set of instructions.
"""
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        directions = {0: [0, 1], 1: [1, 0], 2: [0, -1], 3: [-1, 0]}
        cur = 0
        position = [0, 0]
        for i in instructions:
            if i == "G":
                position[0] += directions[cur][0]
                position[1] += directions[cur][1]
            elif i == "L":
                cur = (cur - 1) % 4
            else:
                cur = (cur + 1) % 4
        if cur != 0 or position == [0, 0]:
            return True
        return False
