"""
BFS
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        queue = [root]
        nextRow = []
        depth = 0
        while queue:
            nextRow = queue[:]
            queue = []
            for node in nextRow:
                queue.extend(node.children)
            depth += 1
        return depth
