"""
@difficulty: medium
@tags: binary tree
@notes: Solution 1 sets the height for each node then use another pass to get result, solution 2 just use one pass.
"""
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def setHeight(root, height):
            if not root:
                return height
            leftHeight = setHeight(root.left, height)
            rightHeight = setHeight(root.right, height)
            root.height = max(leftHeight, rightHeight) + 1
            return root.height
        setHeight(root, 0)
        while root:
            l, r = 0, 0
            if root.left:
                l = root.left.height
            if root.right:
                r = root.right.height
            if l == r:
                return root
            if l > r:
                root = root.left
            else:
                root = root.right
        return root


class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root):
            if not root:
                return root, 0
            left, leftHeight = helper(root.left)
            right, rightHeight = helper(root.right)
            if leftHeight > rightHeight:
                return left, leftHeight + 1
            elif leftHeight < rightHeight:
                return right, rightHeight + 1
            return root, leftHeight + 1
        return helper(root)[0]
