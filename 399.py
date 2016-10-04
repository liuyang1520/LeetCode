"""
For each pair, put value in dictionary as edges in graph.
Use Floyd–Warshall algorithm to update graph.
http://bookshadow.com/weblog/2016/09/11/leetcode-evaluate-division/
"""
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        import collections
        relations = collections.defaultdict(lambda: collections.defaultdict(int))
        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            relations[x][y] = value
            relations[y][x] = 1.0 / value
        res = []
        for k in relations:
            relations[k][k] = 1.0
            for i in relations:
                for j in relations:
                    if relations[i][k] and relations[k][j]:
                        relations[i][j] = relations[i][k] * relations[k][j]
        for x, y in queries:
            if relations[x][y]:
                res.append(relations[x][y])
            else:
                res.append(-1.0)
        return res