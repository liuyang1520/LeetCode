"""
Right - root - left traversal
Store the previous subsum and use it for next recursive call
"""
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def convertBSTHelper(root, subsum):
            if root.right:
                subsum = convertBSTHelper(root.right, subsum)
            root.val += subsum
            if root.left:
                return convertBSTHelper(root.left, root.val)
            return root.val
        
        if not root:
            return root
        
        convertBSTHelper(root, 0)
        return root