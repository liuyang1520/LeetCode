"""
@difficulty: easy
@tags: misc
@notes: Return the value when frequency is more than 25%. Or check whether two elements are same when for arr[i] and arr[i+gap], gap = n / 4.
"""
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                length += 1
            else:
                length = 1
            if length > len(arr) * 0.25:
                return arr[i]
        if length > len(arr) * 0.25:
            return arr[0]
