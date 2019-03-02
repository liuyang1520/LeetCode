"""
Preorder traversal
"""
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(root):
            if not root:
                return ["#"]
            return [str(root.val)] + helper(root.left) + helper(root.right)
        nodes = helper(root)
        return ",".join(nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(',')
        def helper(nodes, i):
            if i >= len(nodes) or nodes[i] == '#':
                return [None, i+1]
            else:
                newNode = TreeNode(nodes[i])
                newNode.left, j = helper(nodes, i+1)
                newNode.right, j = helper(nodes, j)
                return [newNode, j]
        return helper(nodes, 0)[0]
