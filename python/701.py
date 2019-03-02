"""
If root is leaf, assign its left/right directly.
"""
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        rootbk = root
        newNode = TreeNode(val)
        while root:
            if val > root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = newNode
                    break
            elif val < root.val:
                if root.left:
                    root = root.left
                else:
                    root.left = newNode
                    break
        return rootbk
