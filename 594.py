"""
1. Misunderstanding the question at first, was think the sequence has to be continuous,
so using a stack to store the values and pop the first x items when finding new value

2. Real solution, use a dictionary to get all counts of all values
"""
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        print findLHS([1,3,2,2,1,1,5,2,3,7])
        # 4
        """
        maxLen = 0
        if not nums:
            return maxLen
        stack = []
        for i in nums:
            if not stack or abs(stack[-1] - i) > 1:
                stack = [i]
            elif i in stack:
                stack.append(i)
            else:
                j = -1
                for j in range(len(stack)-2, -1, -1):
                    if stack[j] not in [i, stack[-1]]:
                        break
                stack = stack[j+1:] + [i]
            maxLen = max(len(stack), maxLen)
        return maxLen


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter

        if not nums:
            return 0
        counter = Counter(nums)
        keys = sorted(counter.keys())
        maxLen = 0
        for i in range(len(keys)-1):
            if abs(keys[i] - keys[i+1]) == 1:
                maxLen = max(counter[keys[i]] + counter[keys[i+1]], maxLen)
        return maxLen
