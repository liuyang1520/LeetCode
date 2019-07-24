"""
@difficulty: easy
@tags: misc
@notes: First count zeroes, then from end to start, map the value to its new position.
"""
class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        zeroCount = sum(i == 0 for i in arr)
        for i in range(len(arr) - 1, -1, -1):
            if not arr[i]:
                zeroCount -= 1
                if i + zeroCount + 1 < len(arr):
                    arr[i + zeroCount + 1] = arr[i]
            if i + zeroCount < len(arr):
                arr[i + zeroCount] = arr[i]
        return arr
