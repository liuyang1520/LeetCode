"""
Run dfs first to store left and right depth in the TreeNode, then solve the problem by comparing the depths
"""
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def getMaxDepth(root, depth):
            left, right = depth, depth
            if root.left:
                left = getMaxDepth(root.left, depth + 1)
            if root.right:
                right = getMaxDepth(root.right, depth + 1)
            root.leftDepth, root.rightDepth = left, right
            return max(left, right)

        getMaxDepth(root, 0)
        maxDepth = max(root.leftDepth, root.rightDepth)
        while root and (root.leftDepth != root.rightDepth or root.leftDepth == maxDepth - 1 or root.rightDepth == maxDepth - 1):
            if root.leftDepth > root.rightDepth:
                root = root.left
            else:
                root = root.right
        return root
