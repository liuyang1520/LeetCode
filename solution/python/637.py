"""
Iterate the tree level by level
"""
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            res.append(sum([i.val for i in queue]) / float(len(queue)))
            temp = []
            for node in queue:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            queue = temp
        return res
