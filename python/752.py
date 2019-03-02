"""
BFS
"""
class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1
        queue = ['0000']
        visited = set(queue + deadends)
        steps = 0
        while queue:
            temp = []
            for val in queue:
                if val == target:
                    return steps
                for i, v in enumerate(val):
                    for d in (-1, 1):
                        newV = (int(v) + d + 10) % 10
                        newV = val[:i] + str(newV) + val[i+1:]
                        if newV not in visited:
                            visited.add(newV)
                            temp.append(newV)
            queue = temp
            steps += 1
        return -1
