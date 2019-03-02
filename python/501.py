"""
Counter + pre-order traversal
"""
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        import collections
        freq = collections.Counter()
        
        def findModeHelper(root):
            freq[root.val] += 1
            if root.left:
                findModeHelper(root.left)
            if root.right:
                findModeHelper(root.right)

        if not root:
            return []
        findModeHelper(root)
        temp = freq.most_common(1)[0][1]
        return [i for i in freq if freq[i] == temp]