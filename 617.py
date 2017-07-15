"""
My answer seems to be too complex.
Can be improved:
if not t1:
	return t2
if not t2:
	return t1
t = TreeNode(t1.val + t2.val)
t.left = mergeTrees(t1.left, t2.left)
t.right = mergeTrees(t1,right, t2.right)
"""
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1 and not t2:
            return None
        root = TreeNode(0)
        self.mergeTreesHelper(root, t1, t2)
        return root


    def mergeTreesHelper(self, newNode, t1, t2):
        if not t1 and not t2:
            return
        elif not t1 and t2:
            newNode.val = t2.val
            newNode.left, newNode.right = t2.left, t2.right
        elif t1 and not t2:
            newNode.val = t1.val
            newNode.left, newNode.right = t1.left, t1.right
        else:
            newNode.val = t1.val + t2.val
            if t1.left or t2.left:
                newNode.left = TreeNode(0)
                self.mergeTreesHelper(newNode.left, t1.left, t2.left)
            if t1.right or t2.right:
                newNode.right = TreeNode(0)
                self.mergeTreesHelper(newNode.right, t1.right, t2.right)
