"""
@difficulty: easy
@tags: misc
@notes: O(nlogn) for the sorting.
"""
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float('inf')
        res = []
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            minDiff = min(diff, minDiff)
        for i in range(len(arr) - 1):
            if arr[i+1] - arr[i] == minDiff:
                res.append([arr[i], arr[i+1]])
        return res
