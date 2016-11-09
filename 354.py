"""
1. sort + DP, got TLE (n^2)
2. sorted by x[0] ascending x[1] descending, then use the method in "Longest Consecutive Sequence" (nlogn)
"""
class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes = sorted(envelopes)
        dp = [1] * (len(envelopes) + 1)
        dp[0] = 0
        for i in range(2, len(envelopes)+1):
            for j in range(1, i):
                if envelopes[i-1][0] > envelopes[j-1][0] and envelopes[i-1][1] > envelopes[j-1][1] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
        return max(dp)


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, cmp = lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        stack = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            if envelopes[i][1] > stack[-1]:
                stack.append(envelopes[i][1])
                continue
            left, right = 0, len(stack)-1
            while left <= right:
                mid = (left + right) / 2
                if stack[mid] < envelopes[i][1]:
                    left = mid + 1
                else:
                    right = mid - 1
            stack[left] = envelopes[i][1]
        return len(stack)