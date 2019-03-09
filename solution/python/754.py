"""
Solution 1, BFS, got TLE
Solution 2, math
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target == 0: return 0
        queue = [0]
        step = 1
        visited = set()
        while queue:
            nextQueue = []
            node = queue.pop()
            for i in [node+step, node-step]:
                if i == target:
                    return step
                if i not in visited:
                    nextQueue.append(i)
            step += 1
            queue = nextQueue
        return 0

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        n = 1
        while n*(n+1)/2 < target:
            n += 1
        seriesSum = n*(n+1)/2
        if (seriesSum - target) % 2 == 0:
            return n
        elif (n + 1) % 2:
            return n + 1
        else:
            return n + 2
