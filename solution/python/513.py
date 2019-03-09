"""
BFS, keep the last value as the result to return
"""
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        last = None
        while queue:
            node = queue.pop()
            if node.right:
                queue.insert(0, node.right)
            if node.left:
                queue.insert(0, node.left)
            last = node.val
        return last