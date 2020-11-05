"""
@difficulty: easy
@tags: misc
@notes: One iteration, check whether count is below zero.
"""
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == "../":
                count = max(0, count - 1)
            elif log == "./":
                pass
            else:
                count += 1
        return count
