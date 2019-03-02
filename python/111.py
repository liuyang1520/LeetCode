# Recursive solution.
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def minDepthHelp(node, depth):
            if (not node.left) and (not node.right):
                if depth < self.minDepth:
                    self.minDepth = depth
            if node.left:
                minDepthHelp(node.left, depth + 1)
            if node.right:
                minDepthHelp(node.right, depth + 1)
                
        if not root:
            return 0
        self.minDepth = 20000000
        minDepthHelp(root, 1)
        return self.minDepth


# Found 2 beautiful solutions online.
# https://leetcode.com/discuss/51384/python-bfs-and-dfs-solutions
# DFS
def minDepth1(self, root):
    if not root:
        return 0
    if None in [root.left, root.right]:
        return max(self.minDepth(root.left), self.minDepth(root.right)) + 1
    else:
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# BFS   
def minDepth(self, root):
    if not root:
        return 0
    queue = collections.deque([(root, 1)])
    while queue:
        node, level = queue.popleft()
        if node:
            if not node.left and not node.right:
                return level
            else:
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))