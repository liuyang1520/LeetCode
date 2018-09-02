"""
preorder: https://github.com/liuyang1520/LeetCode/blob/master/114.py
inorder: https://github.com/liuyang1520/LeetCode/blob/master/94.py
postorder: https://github.com/liuyang1520/LeetCode/blob/master/145.py

See inorder for more solutions.
The prev is tracking the previous tree node to avoid infinite loop.
"""
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack = [root]
        prev = None
        rootBackup = rootNew = TreeNode(0)
        while stack:
            peek = stack[-1]
            if peek.left and ((not prev) or (prev and prev.left == peek) or (prev and prev.right == peek)):
                stack.append(peek.left)
            else:
                stack.pop()
                rootNew.right = TreeNode(peek.val)
                rootNew = rootNew.right
                if peek.right:
                    stack.append(peek.right)
            prev = peek
        return rootBackup.right
