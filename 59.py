# Use direction variable to determine where to go. Use left, right, up, down to determine the edges.
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for i in range(n)]
        left = up = 0
        right = down = n - 1
        x = y = 0
        direction = "right"
        num = 1
        while num <= n * n and left <= right and up <= down:
            res[y][x] = num
            if direction == "right":
                if x <= right - 1:
                    x += 1
                    num += 1
                else:
                    direction = "down"
                    up += 1
            elif direction == "down":
                if y <= down - 1:
                    y += 1
                    num += 1
                else:
                    direction = "left"
                    right -= 1
            elif direction == "left":
                if x >= left + 1:
                    x -= 1
                    num += 1
                else:
                    direction = "up"
                    down -= 1
            else:
                if y >= up + 1:
                    y -= 1
                    num += 1
                else:
                    direction = "right"
                    left += 1
        return res