"""
Count the most common right edges, it should be the correct position to cut
"""
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edge = {}
        for row in wall:
            temp = 0
            for i in range(len(row)-1):
                temp += row[i]
                if temp not in edge:
                    edge[temp] = 1
                else:
                    edge[temp] += 1
        if not edge:
            return len(wall)
        return len(wall) - max(edge.values())
