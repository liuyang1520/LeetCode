"""
Solution 1:
1) Find all leaf nodes, and store them in a list;
2) Delete all nodes in that list;
3) Repeat 1, 2 until 1 or 2 nodes are remained.
Using adjacent list (set) to represent graph.

Solution 2:
1) Choose a random node R as root, use BFS or DFS to find node A with longest path from R;
2) Choose A as root, use BFS or DFS to find node B with longest path from A;
3) Find the middle node (1 or 2 nodes) of path A -> B as the answer.
"""
# Time Limit Exceeded, use matrix to represent graph, cost too much time to query
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = [[0] * n for i in range(n)]
        for edge in edges:
            graph[edge[0]][edge[1]] = 1
            graph[edge[1]][edge[0]] = 1
        nodes = range(n)
        while len(nodes) > 2:
            deletes = []
            for i in nodes:
                if sum(graph[i]) <= 1:
                    deletes.append((i, graph[i].index(1)))
            while deletes:
                node = deletes.pop()
                graph[node[1]][node[0]] = 0
                nodes.remove(node[0])
        return nodes

# Found a solution using set (as linked list) to represent graph and got AC
# https://discuss.leetcode.com/topic/30572/share-some-thoughts/2
def findMinHeightTrees(self, n, edges):
    if n == 1: return [0] 
    adj = [set() for _ in xrange(n)]
    for i, j in edges:
        adj[i].add(j)
        adj[j].add(i)

    leaves = [i for i in xrange(n) if len(adj[i]) == 1]

    while n > 2:
        n -= len(leaves)
        newLeaves = []
        for i in leaves:
            j = adj[i].pop()
            adj[j].remove(i)
            if len(adj[j]) == 1: newLeaves.append(j)
        leaves = newLeaves
    return leaves