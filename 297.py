"""
Solution 1:
Got TLE
BFS + Perfect Binary Tree
    1
   / \
  2   3
     / \
    4   5
         \
          6
[                       1,
            2,                  3,
    null,       null,       4,          5
null, null, null, null, null, null, null,  6]

The advantage is to reconstruct the tree:
    nodes[i].left = nodes[2*i + 1]
    nodes[i].right = nodes[2*i + 2]
Disadvantage is too slow, and additional storing space.


Solution 2:
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
BFS + Full Binary Tree
    1
   / \
  2   3
     / \
    4   5
         \
          6
[                       1,
            2,                  3,
    null,       null,       4,          5
                        null, null, null,  6]

"""

# Solution 1
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return []
        level_cur = [root]
        valid = True
        while valid:
            valid = False
            temp, level_next = [], []
            for node in level_cur:
                if node:
                    valid = True
                    temp.append(node.val)
                    level_next.extend([node.left, node.right])
                else:
                    temp.append("null")
                    level_next.extend([None, None])
            if valid:
                res.extend(temp)
            level_cur = level_next
        return ",".join(map(str, res))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split(",")
        nodes = [TreeNode(int(i)) if i != "null" else None for i in data]
        for i in range(0, (len(nodes) - 1) / 2):
            if nodes[i]:
                nodes[i].left = nodes[2*i + 1]
                nodes[i].right = nodes[2*i + 2]
        return nodes[0]

# Solution 2
class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        if not root:
            return []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                queue.extend([node.left, node.right])
                res.append(node.val)
            else:
                res.append("null")
        return ",".join(map(str, res))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return
        data = data.split(",")
        queue = []
        root = TreeNode(data[0])
        temp = root
        for i in range(1, len(data)):
            odd = bool(i % 2)
            if data[i] == "null":
                if not odd and queue:
                    temp = queue.pop(0)
                continue
            node = TreeNode(data[i])
            queue.append(node)
            if odd:
                temp.left = node
            else:
                temp.right = node
                temp = queue.pop(0)
        return root