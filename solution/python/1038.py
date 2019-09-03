"""
@difficulty: medium
@tags: DFS
@notes: Recursively calculate the sums based on right, root, left order.
"""
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.right:
            self.bstToGst(root.right)
            temp = root.right
            while temp.left:
                temp = temp.left
            root.val += temp.val
        if root.left:
            temp = root.left
            while temp.right:
                temp = temp.right
            temp.val += root.val
            self.bstToGst(root.left)
        return root
