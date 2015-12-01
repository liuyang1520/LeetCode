# BFS.
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            length = len(queue)
            nums = []
            for i in range(length):
                root = queue.pop()
                nums.append(root.val)
                if root.left:
                    queue.insert(0, root.left)
                if root.right:
                    queue.insert(0, root.right)
            res.append(nums)
        return res