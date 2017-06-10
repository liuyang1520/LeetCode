"""
This problem is confusing, not sure why omitting the nulls in "[1,2,3,null,null,null,4]" test case.
"""
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        if not t.right:
            return str(t.val) + "({})".format(self.tree2str(t.left))
        return str(t.val) + "({left})({right})".format(left = self.tree2str(t.left), right = self.tree2str(t.right))
