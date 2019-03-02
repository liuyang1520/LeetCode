"""
Recursively create the quad tree. Node the x, y is opposite to the question's grid expression.
"""
"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def isLeaf(xmin, xmax, ymin, ymax):
            val = grid[xmin][ymin]
            for x in range(xmin, xmax + 1):
                for y in range(ymin, ymax + 1):
                    if grid[x][y] != val:
                        return False
            return True
        
        def helper(xmin, xmax, ymin, ymax):
            root = Node('*', False, None, None, None, None)
            if isLeaf(xmin, xmax, ymin, ymax):
                root.isLeaf = True
                root.val = bool(grid[xmin][ymin])
            else:
                root.topLeft = helper(xmin, (xmin + xmax) / 2, ymin, (ymin + ymax) / 2)
                root.bottomLeft = helper((xmin + xmax) / 2 + 1, xmax, ymin, (ymin + ymax) / 2)
                root.topRight = helper(xmin, (xmin + xmax) / 2, (ymin + ymax) / 2 + 1, ymax)
                root.bottomRight = helper((xmin + xmax) / 2 + 1, xmax, (ymin + ymax) / 2 + 1, ymax)
            return root

        return helper(0, len(grid)-1, 0, len(grid[0])-1)
