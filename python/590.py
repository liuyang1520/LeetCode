"""
See https://github.com/liuyang1520/LeetCode/blob/master/145.py
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        stack = [root]
        visited = set()
        while stack:
            peek = stack[-1]
            if peek and peek.children and peek not in visited:
                stack.extend(peek.children[::-1])
            else:
                res.append(stack.pop().val)
            visited.add(peek)
        return res
