"""
Dijkstra's algorithm, https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
"""
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        vertex = set()
        dist = [0] * N
        for i in range(1, N + 1):
            dist[i-1] = float('inf')
            vertex.add(i)
        dist[K-1] = 0
        for u, v, w in times:
            if u == K:
                dist[v-1] = w
        while vertex:
            minDist = float('inf')
            for node in vertex:
                if dist[node-1] < minDist:
                    minNode, minDist = node, dist[node-1]
            if minDist == float('inf'):
                return -1
            vertex.discard(minNode)
            for u, v, w in times:
                if u == minNode:
                    dist[v-1] = min(dist[v-1], minDist + w)
            print dist, vertex
        if max(dist) == float('inf'):
            return -1
        else:
            return max(dist)
