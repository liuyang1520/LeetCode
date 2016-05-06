# DP problem, using recursive solution. My first trial got "Time Limit Exceeded".
# Second solution (https://www.hrwhisper.me/leetcode-house-robber-iii/) directly compute the value instead of using flag var.
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return self.robHelper(root, True)
        
        
    def robHelper(self, root, flag):
        if (not root.left) and (not root.right):
            return root.val if flag else 0
        if (not root.left) and root.right:
            if flag:
                return max(root.val + self.robHelper(root.right, False), self.robHelper(root.right, True))
            else:
                return self.robHelper(root.right, True)
        if (not root.right) and root.left:
            if flag:
                return max(root.val + self.robHelper(root.left, False), self.robHelper(root.left, True))
            else:
                return self.robHelper(root.left, True)
        if flag:
            return max(root.val + self.robHelper(root.left, False) + self.robHelper(root.right, False), self.robHelper(root.left, True) + self.robHelper(root.right, True))
        else:
            return self.robHelper(root.left, True) + self.robHelper(root.right, True)


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.robHelper(root)[0]
        
        
    def robHelper(self, root):
        if not root:
            return 0, 0
        left, leftNotChoose = self.robHelper(root.left)
        right, rightNotChoose = self.robHelper(root.right)
        return max(root.val + leftNotChoose + rightNotChoose, left + right), left + right
                

