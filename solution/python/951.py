"""
@difficulty: easy
@tags: tree, DFS
@notes: Compare the left and right nodes recursively.
"""
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
            return False
        if (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.right, root2.left) and self.flipEquiv(root1.left, root2.right)):
            return True
        return False
