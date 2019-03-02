"""
This solution is topological sort (similar to BFS), not sure why it is so slow comparing to DFS.
The official solution 1 is same as here, 2 is the DFS one.
"""
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        length = len(graph)
        outgoings = [set(i) for i in graph]
        incomings = [set() for _ in range(length)]
        res = set()
        lastChanges = set()
        for i, val in enumerate(graph):
            if not val:
                lastChanges.add(i)
            for j in val:
                incomings[j].add(i)
        while lastChanges:
            removedNodes = set()
            for i in lastChanges:
                if len(outgoings[i]) == 0:
                    removedNodes.add(i)
            # update graph to remove edges outgoing to terminals
            # store the changed nodes into temp, and only need to search termnials
            # inside the temp set
            temp = set()
            for i in removedNodes:
                res.add(i)
                for j in incomings[i]:
                    outgoings[j] -= removedNodes
                    temp.add(j)
            lastChanges = temp
        return sorted(res)
