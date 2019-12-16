"""
@difficulty: medium
@tags: misc
@notes: Be careful of the orders.
"""
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        x, y = king
        # Up
        for i in range(x-1, -1, -1):
            if [i, y] in queens:
                res.append([i, y])
                break
        # Down
        for i in range(x+1, 8):
            if [i, y] in queens:
                res.append([i, y])
                break
        # Left
        for j in range(y-1, -1, -1):
            if [x, j] in queens:
                res.append([x, j])
                break
        # Right
        for j in range(y+1, 8):
            if [x, j] in queens:
                res.append([x, j])
                break
        # NW
        for i in range(1, min(x, y)+1):
            if [x-i, y-i] in queens:
                res.append([x-i, y-i])
                break
        # SE
        for i in range(1, 8 - max(x, y)):
            if [x+i, y+i] in queens:
                res.append([x+i, y+i])
                break
        # SW
        for i in range(1, 8):
            xn, yn = x + i, y - i
            if xn > 8 or yn < 0:
                break
            if [xn, yn] in queens:
                res.append([xn, yn])
                break
        # NE
        for i in range(1, 8):
            xn, yn = x - i, y + i
            if xn < 0 or yn > 8:
                break
            if [xn, yn] in queens:
                res.append([xn, yn])
                break
        return res
