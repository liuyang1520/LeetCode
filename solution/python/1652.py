"""
@difficulty: easy
@tags: sliding window
@notes: straight-forward solution.
"""
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        length = len(code)
        doubleCode = code * 2
        if k > 0:
            index = 0
            res = [sum([doubleCode[i] for i in range(index + 1, index + 1 + k)])]
            for i in range(1, length):
                res.append(res[-1] + doubleCode[i+k] - doubleCode[i])
            return res
        elif k < 0:
            index = length
            res = [sum([doubleCode[i] for i in range(index - 1, index - 1 + k, -1)])]
            for i in range(index + 1, index + length):
                res.append(res[-1] - doubleCode[i+k-1] + doubleCode[i-1])
            return res
        else:
            return [0] * length
