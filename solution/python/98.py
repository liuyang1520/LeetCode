# Traverse the tree to a list, then find it sorted or not.
# Method 2:
# Recursively compare the nodes in the tree, [value of left nodes] < root.val and root.val < [value of right nodes].
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def isValidBSTHelper(node):
            temp = [node.val]
            if node.left:
                temp = isValidBSTHelper(node.left) + temp
            if node.right:
                temp = temp + isValidBSTHelper(node.right)
            return temp
        res = isValidBSTHelper(root)
        for i in range(len(res) - 1):
            if res[i] >= res[i + 1]:
                return False
        return True