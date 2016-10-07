"""
DFS, Eulerian path
Solution 1: DFS
Solution 2: Hierholzer Algorithm
    https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c/2
"""
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        route = defaultdict(lambda: defaultdict(int))
        for start, end in tickets:
            route[start][end] += 1
        start = "JFK"
        length = len(tickets) + 1
        res = [start]
        
        def dfs(start, route):
            if len(res) == length:
                return True
            if start in route:
                for i in sorted(route[start].keys()):
                    if route[start][i] > 0:
                        res.append(i)
                        route[start][i] -= 1
                        if dfs(i, route):
                            return True
                        res.pop()
                        route[start][i] += 1
        dfs(start, route)       
        return res

    # Hierholzer Algorithm
    def findItinerary(self, tickets):
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
        visit('JFK')
        return route[::-1]