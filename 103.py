"""
Note: queue[::-1] and left,right to right,left
"""
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = [root]
        odd = False
        while queue:
            odd = not odd
            level = queue[::-1]
            queue, temp = [], []
            for i in level:
                temp += [i.val]
                if odd:
                    if i.left: queue.append(i.left)
                    if i.right: queue.append(i.right)
                else:
                    if i.right: queue.append(i.right)
                    if i.left: queue.append(i.left)
            res.append(temp)
        return res