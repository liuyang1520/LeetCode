"""
@difficulty: easy
@tags: misc
@notes: Special case when num is 0.
"""
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numSet = set(arr)
        for i in numSet:
            if i * 2 in numSet:
                if i == 0:
                    if arr.count(0) >= 2:
                        return True
                else:
                    return True
        return False
