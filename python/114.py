# Preorder traversal of binary tree.
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        while stack:
            node = stack.pop()
            if node != root:
                root.right = node
                root.left = None
                root = root.right
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


# In-place solution. Rotate the right subtree to the rightmost leaf of left subtree, iteratively.
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                rootLeft = root.left
                while rootLeft.right:
                    rootLeft = rootLeft.right
                rootLeft.right = root.right
                root.right = root.left
                root.left = None
            root = root.right


# recursive solution
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        res = [root.val]
        if root.left:
            res += self.preorderTraversal(root.left)
        if root.right:
            res += self.preorderTraversal(root.right)
        return res
