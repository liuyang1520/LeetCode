"""
If a node is not none, then recursively compare itself, left, right, to the subtree t.
When compare two subtrees, recursively compare the root value, left, then right.

Another solution is to flatten trees into strings then compare two string.
Need to a special strings for distinguish parent, child, and empty nodes.
"""
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return bool(s) and (self.compareBinTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))


    def compareBinTree(self, r1, r2):
        if not r1 and not r2:
            return True
        if (not r1 and r2) or (not r2 and r1):
            return False
        return r1.val == r2.val and self.compareBinTree(r1.left, r2.left) and self.compareBinTree(r1.right, r2.right)
