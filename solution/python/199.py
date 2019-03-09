# BFS.
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        queue = [root]
        nums = []
        while queue:
            tempQueue = []
            for i in range(len(queue)):
                root = queue.pop()
                if i == 0:
                    nums.append(root.val)
                if root.right:
                    tempQueue.insert(0, root.right)
                if root.left:
                    tempQueue.insert(0, root.left)
            queue = tempQueue
        return nums