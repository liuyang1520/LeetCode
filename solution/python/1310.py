"""
@difficulty: medium
@tags: misc
@notes: Store the Xor(1~n) as array to quick calculation, subXorList[x-1] ^ subXorList[y].
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        subXorList, subXor = [], 0
        for i in range(len(arr)):
            subXor ^= arr[i]
            subXorList.append(subXor)
        res = []
        for x, y in queries:
            if x == 0:
                res.append(subXorList[y])
            else:
                res.append(subXorList[x-1] ^ subXorList[y])
        return res
