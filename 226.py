# Recursive solution.
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root


# Non-recursive solution.
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = []
        stack.append(root)
        if root == None:
            return None
        while stack:
            currentNode = stack.pop()
            if currentNode.left:
                stack.append(currentNode.left)
            if currentNode.right:
                stack.append(currentNode.right)
            currentNode.left, currentNode.right = currentNode.right, currentNode.left
        return root