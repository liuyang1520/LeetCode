"""
Need to check whether a node can be treated as start point:
1. use dictionary to track, get TLE, pathSumHelper(self, root, subsum, start)
2. use bool flag to track, pathSumHelper(self, root, subsum, flag)
"""
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.sum = sum
        self.res = 0
        if root:
            self.pathSumHelper(root, 0, True)
        return self.res
        
    def pathSumHelper(self, root, subsum, flag):
        if root.left:
            self.pathSumHelper(root.left, subsum + root.val, False)
            if flag:
                self.pathSumHelper(root.left, 0, True)
        if root.right:
            self.pathSumHelper(root.right, subsum + root.val, False)
            if flag:
                self.pathSumHelper(root.right, 0, True)
        if subsum + root.val == self.sum:
            self.res += 1
            return