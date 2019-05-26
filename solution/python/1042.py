"""
@difficulty: medium
@tags: greedy
@notes: Solution 1 got TLE, overthinking;
Solution 2 greedily paint the gradens since "no garden that has more than 3 paths coming into or leaving it".
"""
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        connects = {}
        for i, j in paths:
            if i in connects:
                connects[i].append(j)
            else:
                connects[i] = [j]
            if j in connects:
                connects[j].append(i)
            else:
                connects[j] = [i]
        paints = {}
        queue = [1]
        while len(paints) < N:
            if queue:
                first = queue.pop(0)
            else:
                for i in range(1, N+1):
                    if i not in paints:
                        first = i
                        break
            used = set()
            for n in connects.get(first, []):
                if n not in paints:
                    queue.append(n)
                else:
                    used.add(paints[n])
            for i in range(1, 5):
                if i not in used:
                    paints[first] = i
                    break
        return [paints[i] for i in range(1, N+1)]


class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        paints = [0] * N
        graph = [[] for i in range(N)]
        for i, j in paths:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        for i in range(N):
            paints[i] = ({1, 2, 3, 4} - set(paints[node] for node in graph[i])).pop()
        return paints
