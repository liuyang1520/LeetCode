# Get the paths of post-order traversal, from root to target. Find the first distinct element in the two path.
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path1 = self.rootToTargetPath(root, p)
        path2 = self.rootToTargetPath(root, q)
        node = None
        pos = 0
        while pos < len(path1) and pos < len(path2) and path1[pos] == path2[pos]:
            node = path1[pos]
            pos += 1
        return node
            
        
    def rootToTargetPath(self, root, target):
        stack = []
        previous = None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                peek = stack[-1]
                if peek.right and peek.right != previous:
                    root = peek.right
                else:
                    if peek == target:
                        return stack
                    previous = stack.pop()
                    root = None