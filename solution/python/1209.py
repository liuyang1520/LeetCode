"""
@difficulty: medium
@tags: stack
@notes: Solution 1 uses stack by pushing chars and gets TLE, Solution 2 only counts the chars and pushes to stack.
"""
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            stack.append(char)
            hasAdjDup = True
            if len(stack) >= k:
                i = len(stack) - k
                for j in range(i, len(stack)):
                    if stack[i] != stack[j]:
                        hasAdjDup = False
                        break
                if hasAdjDup:
                    stack = stack[:i]
        return "".join(stack)


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            stack.append([char, 1])
            hasAdjDup = True
            if len(stack) >= 2:
                if stack[-1][0] == stack[-2][0]:
                    _, count = stack.pop()
                    stack[-1][1] += count
                if stack[-1][1] == k:
                    stack.pop()
        return "".join(map(lambda x: x[0]*x[1], stack))
