# Use a stack to trace current and paths.
class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        paths = []
        if not root:
            return paths
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if (not node.left) and (not node.right):
                paths.append(path)
            elif node.left and (not node.right):
                stack.append([node.left, path + "->" + str(node.left.val)])
            elif node.right and (not node.left):
                stack.append([node.right, path + "->" + str(node.right.val)])
            else:
                stack.append([node.left, path + "->" + str(node.left.val)])
                stack.append([node.right, path + "->" + str(node.right.val)])
        return paths