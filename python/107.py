# Use two queues, one for current layer, one for next layer.
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        levelQueue = []
        res = [[root.val]]
        while queue:
            cur = queue.pop()
            if cur.left:
                levelQueue.insert(0, cur.left)
            if cur.right:
                levelQueue.insert(0, cur.right)
            if not queue:
                if levelQueue:
                    res.append([i.val for i in levelQueue[::-1]])
                queue[:] = levelQueue
                levelQueue = []
        return res[::-1]