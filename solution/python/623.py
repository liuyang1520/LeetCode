"""
Tree level by level traversal
"""
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            temp = TreeNode(v)
            temp.left = root
            return temp
        queue = [root]
        depth = 1
        while queue:
            nextQueue = []
            if depth == d - 1:
                for node in queue:
                    temp = TreeNode(v)
                    temp.left, node.left = node.left, temp
                    temp = TreeNode(v)
                    temp.right, node.right = node.right, temp
                return root
            for node in queue:
                if node.left:
                    nextQueue.append(node.left)
                if node.right:
                    nextQueue.append(node.right)
            queue = nextQueue
            depth += 1
        return root
