"""
@difficulty: easy
@tags: misc
@notes: brute-force
"""
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        count = 0
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        count += 1
        return count
