"""
Recursively retrive the subsum values and updated the counts in a dictionary.
"""
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        from collections import Counter

        counter = Counter()

        def findTreeSumHelper(root):
            if not root: return 0
            temp = root.val + findTreeSumHelper(root.left) + findTreeSumHelper(root.right)
            counter[temp] += 1
            return temp

        if not root: return []
        findTreeSumHelper(root)
        maxFreq = counter.most_common(1)[0][1]
        return [i for i, j in counter.items() if j == maxFreq]
