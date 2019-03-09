# Recursive solution.
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if (not root.left) and (not root.right) and root.val == sum:
            return True
        if root.left and self.hasPathSum(root.left, sum - root.val):
            return True
        if root.right and self.hasPathSum(root.right, sum - root.val):
            return True
        return False


# Iterative solution, preorder traversal.
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            root, total = stack.pop()
            if total == sum and (not root.left) and (not root.right):
                return True
            if root.left:
                stack.append((root.left, total + root.left.val))
            if root.right:
                stack.append((root.right, total + root.right.val))
        return False