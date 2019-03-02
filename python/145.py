# Recursive solution.
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        if root.left:
            res += self.postorderTraversal(root.left)
        if root.right:
            res += self.postorderTraversal(root.right)
        res += [root.val]
        return res


# Post-order traversal is the reverse of root->right->left (preorder traversal variation).
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return res[::-1]


# Refer to http://bookshadow.com/weblog/2015/01/19/leetcode-binary-tree-postorder-traversal/.
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        pre = None
        while stack:
            root = stack[-1]
            if pre is None or pre.left == root or pre.right == root:
                if root.left:
                    stack.append(root.left)
                elif root.right:
                    stack.append(root.right)
            elif root.left == pre and root.right:
                stack.append(root.right)
            else:
                stack.pop()
                res.append(root.val)
            pre = root
        return res