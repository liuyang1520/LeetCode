"""
preorder: [root, left_part, right_part]
postorder: [left_part, right_part, root]
Recursively construct the tree by separating the parts
"""
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        def helper(pre, post):
            if not pre:
                return None
            root = TreeNode(pre[0])
            if len(pre) == 1:
                return root
            leftRoot, length = pre[1], post.index(pre[1]) + 1
            root.left = helper(pre[1:length+1], post[:length])
            root.right = helper(pre[length+1:], post[length:-1])
            return root
            
        return helper(pre, post)
