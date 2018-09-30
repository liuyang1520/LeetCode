"""
DP knapsack problem
Solution 1 got MLE, memorized recursive solution
Solution 2, DP, from buttom up, dp[i][j] means the max with i zeroes and j ones for current level
Note, need to update the values in reverse order like range(m, zeroes-1, -1), to avoid the updated values to influence the result.
Or can update level by level, with a temp array to store the values.
"""
class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        stats = [(s.count('0'), s.count('1')) for s in strs]
        visited = {}
        def helper(k, m, n):
            if k < 0:
                return 0
            if (k, m, n) in visited:
                return visited[(k, m, n)]
            temp = 0
            temp = max(temp, helper(k-1, m, n))
            if m >= stats[k][0] and n >= stats[k][1]:
                temp = max(temp, helper(k-1, m-stats[k][0], n-stats[k][1]) + 1)
            visited[(k, m, n)] = temp
            return temp
        return helper(len(strs) - 1, m, n)


class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0] * (n+1) for i in range(m+1)]
        for s in strs:
            zeroes, ones = s.count('0'), s.count('1')
            for i in range(m, zeroes-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i-zeroes][j-ones] + 1, dp[i][j])
        return dp[-1][-1]
