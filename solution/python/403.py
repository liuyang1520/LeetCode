"""
DP or BFS or DFS
Use dictionary to save time
"""
class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        from collections import defaultdict as dfdict
        visited = dfdict(lambda: dfdict(bool))
        queue = [(0, 0)]
        stoneSet = set(stones)
        visited[0][0] = True
        while queue:
            x, y = queue.pop(0)
            if x == stones[-1]: return True
            for i in (max(y - 1, 0), y, y + 1):
                if not visited[x + i][i] and (x + i) in stoneSet:
                    visited[x + i][i] = True
                    queue.append((x + i, i))
        return False