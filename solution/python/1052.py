"""
@difficulty: medium
@tags: sliding window
@notes: First calculate xor of customers and grumpy, then use a sliding window to calculate the max consecutive sub-sums.
"""
class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        length = len(customers)
        init = 0
        for i in range(length):
            init += customers[i] if not grumpy[i] else 0
            customers[i] = customers[i] * grumpy[i]
        maxsum = subsum = sum(customers[:X])
        for i in range(X, length):
            subsum += customers[i] - customers[i-X]
            maxsum = max(maxsum, subsum)
        return maxsum + init
