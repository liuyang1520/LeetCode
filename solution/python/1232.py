"""
@difficulty: easy
@tags: math
@notes: Check slope for line function.
"""
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (coordinates[1][0] - coordinates[0][0]) == 0:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
        slope = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        for i in range(2, len(coordinates)):
            if (coordinates[i][0] - coordinates[i-1][0]) == 0 or (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]) != slope:
                return False
        return True
