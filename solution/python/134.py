# Naive solution O(n^2) gets "Time Limit Exceeded".
# The tricky solutions is:
# 1) if sum(gas) < sum(cost), there is no solution;
# 2) from i to j, if sum(i -> j) < 0, then cannot start at any point in this range.
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total = subTotal = 0
        index = -1
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            subTotal += gas[i] - cost[i]
            if subTotal < 0:
                index = i
                subTotal = 0
        if total < 0:
            return -1
        else:
            return index + 1