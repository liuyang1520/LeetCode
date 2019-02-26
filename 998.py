"""
Only need to check the right-most branch to insert the val.
"""
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        _root = root
        if root.val < val:
            temp = TreeNode(val)
            temp.left = root
            return temp
        while True:
            if not root.right:
                root.right = TreeNode(val)
                break
            elif val > root.right.val:
                temp = root.right
                root.right = TreeNode(val)
                root.right.left = temp
                break
            else:
                root = root.right
        return _root
