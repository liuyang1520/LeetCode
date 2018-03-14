"""
DFS
"""
class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def helper(path, node, n):
            for i in graph[node]:
                if i == n:
                    res.append(path + [node, n])
                else:
                    helper(path + [node], i, n)

        n = len(graph) - 1
        res = []
        helper([], 0, n)
        return res
