# The helper function returns False when subtrees are not balanced, return depth otherwise.
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return bool(self.isBalancedHelp(root))
            
    def isBalancedHelp(self, root):
        if root is None:
            return 1
        left = self.isBalancedHelp(root.left)
        right = self.isBalancedHelp(root.right)
        if not (left and right):
            return False
        elif abs(left - right) > 1:
                return False
        else:
            return 1 + max(left, right)