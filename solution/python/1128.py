"""
@difficulty: easy
@tags: misc
@notes: Use string "i,j" or "ij" or int i*10+j or (i,j) as key to count the pairs with hashmap.
"""
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        count = 0
        stats = {}
        for i, j in dominoes:
            i, j = min(i, j), max(i, j)
            if (i, j) in stats:
                count += stats[(i, j)]
                stats[(i, j)] += 1
            else:
                stats[(i, j)] = 1
        return count
