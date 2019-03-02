"""
1. Traverse the tree, for each node, compare it with its largest smaller value and smallest larger value in both left and right subtrees
2. Inorder traversal
"""
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.minDiff = float('inf')
        self.helper(root)
        return self.minDiff

    def helper(self, root):
        if root.left:
            rightMostNode = root.left
            while rightMostNode.right:
                rightMostNode = rightMostNode.right
            self.minDiff = min(self.minDiff, abs(root.val - rightMostNode.val))
            self.helper(root.left)
        if root.right:
            leftMostNode = root.right
            while leftMostNode.left:
                leftMostNode = leftMostNode.left
            self.minDiff = min(self.minDiff, abs(root.val - leftMostNode.val))
            self.helper(root.right)
