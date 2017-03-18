"""
Attempt 1

N   Output
1   1
2   2
3   3
4   3+1+1+1=6
5   4+1+2+1=8
6   5+2+1+3+2*3+1=18

When add N 5->6:
1 2 3 4 5 6
1 [1,2,3,4,5] 6
2 [2, 4] 6
3 [3] 6

1 + 1 + 1 + 1 + 3 + 3 = 10
"""
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0] * (N+1)
        for i in range(1, N+1):
            dp[i] += dp[i-1]
            # add whatever is divisible
            divisibleList = []
            for j in range(1, i):
                if i % j == 0: dp[i] += 1
                divisibleList.append(j)
            # get the groups of divisible values
            divisibleCount = {}
            for j in range(1, i):
                divisibleCount[j] = 0
                for k in range(j+1, i):
                    if k % j == 0: divisibleCount[j] += 1
            # add divisible combinations
            # fails in this condition


"""
[1,2,3,4]
for position 1:
    if we choose 1: then we need to go through [2,3,4] for positions 2-4
    if we choose 2: then we need to go through [1,3,4] for positions 2-4
    ...
Use a hash table to store the values we already explored.
"""
class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        memoriesDict = {}
        def countArrangementHelper(index, restNums):
            if not restNums:
                return 1
            if (index, tuple(restNums)) in memoriesDict:
                return memoriesDict[(index, tuple(restNums))]
            count = 0
            for i, value in enumerate(restNums):
                if value % index == 0 or index % value == 0:
                    count += countArrangementHelper(index + 1, restNums[:i] + restNums[i+1:])
            memoriesDict[(index, tuple(restNums))] = count
            return count
        return countArrangementHelper(1, range(1, N+1))