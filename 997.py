"""
@difficulty: easy
@tags: graph, hashmap
@notes: Use hashmap of sets to calculate the incoming edges.
Another solution would be for each edge, count the indegree - outdegree.
Note this only works if there are no duplicate [i, j] in trust.
"""
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if not trust: return 1
        from collections import defaultdict
        stats, exclusions = defaultdict(set), set([i for i, _ in trust])
        for i, j in trust:
            stats[j].add(i)
            if len(stats[j]) == N - 1 and j not in exclusions:
                return j
        return -1
