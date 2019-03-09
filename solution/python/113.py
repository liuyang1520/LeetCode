"""
DFS
"""
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def pathSumHelper(root, subsum, seq):
            if root.left:
                pathSumHelper(root.left, subsum + root.val, seq + [root.val])
            if root.right:
                pathSumHelper(root.right, subsum + root.val, seq + [root.val])
            if not root.left and not root.right and subsum + root.val == sum:
                res.append(seq + [root.val])
            return
        
        res = []
        if not root:
            return []
        pathSumHelper(root, 0, [])
        return res