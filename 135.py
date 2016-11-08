"""
1. greedy set to 1 for all elements;
2. update from left to right;
3. update from right to left.
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        greedy = [1] * len(ratings)
        # from left to right, update greedy[i+1] = greedy[i] + (ratings[i+1] > ratings[i])
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                greedy[i] = greedy[i-1] + 1
        # from right to left, update greedy[i] = max(greedy[i+1] + (ratings[i] > ratings[i+1]), greedy[i])
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                greedy[i] = max(greedy[i+1] + 1, greedy[i])
        return sum(greedy)