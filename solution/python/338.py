# [valueOf(4), valueOf(5), valueOf(6), valueOf(7)] = [valueOf(0) + 1, valueOf(1) + 1, valueOf(2) + 1, valueOf(3) + 1], from base to num.
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        res = [0] * (num + 1)
        res[1] = 1
        pos = 1
        while pos < num:
            left = pos + 1
            right = left + pos
            for i in range(left, min(right, num) + 1):
                res[i] = res[i - pos - 1] + 1
            pos = pos * 2 + 1
        return res[:num + 1]
