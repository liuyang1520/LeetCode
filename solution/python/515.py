"""
BFS, calcualte max number for each row iteratively.
"""
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        rowQueue = []
        result = [root.val]
        while queue:
            node = queue.pop()
            if node.right:
                rowQueue.append(node.right)
            if node.left:
                rowQueue.append(node.left)
            if not queue and rowQueue:
                queue = rowQueue
                result.append(reduce(lambda x, y: x if x.val > y.val else y, rowQueue).val)
                rowQueue = []
        return result