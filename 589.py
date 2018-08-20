class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            last = stack.pop()
            res.append(last.val)
            if last.children:
                stack.extend(last.children[::-1])
        return res
