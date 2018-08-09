"""
Use 'D' to divide levels
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = [[]]
        queue = [root, 'D']
        while len(queue) > 1:
            head = queue.pop(0)
            if head == 'D':
                queue.append('D')
                res.append([])
            else:
                res[-1].append(head.val)
                if head.children:
                    queue.extend(head.children)
        return res
