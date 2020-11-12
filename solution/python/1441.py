"""
@difficulty: easy
@tags: misc
@notes: Use a pointer to track the position of target.
"""
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        pointer = 0
        res = []
        for i in range(1, n + 1):
            if pointer == len(target):
                break
            if target[pointer] == i:
                res.append("Push")
                pointer += 1
            else:
                res.extend(["Push", "Pop"])
        return res
