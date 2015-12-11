# DFS method.
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nums = [i for i in range(1, n + 1)]
        return self.generateTreesHelp(nums)
        
        
    def generateTreesHelp(self, nums):
        res = []
        if len(nums) <= 0:
            return []
        if len(nums) == 1:
            return [TreeNode(nums[0])]
        for i in range(len(nums)):
            leftSub = self.generateTreesHelp(nums[:i])
            rightSub = self.generateTreesHelp(nums[i+1:])
            if (not leftSub) and rightSub:
                for right in rightSub:
                    root = TreeNode(nums[i])
                    root.right = right
                    res.append(root)
            if (not rightSub) and leftSub:
                for left in leftSub:
                    root = TreeNode(nums[i])
                    root.left = left
                    res.append(root)
            if leftSub and rightSub:
                for left in leftSub:
                    for right in rightSub:
                        root = TreeNode(nums[i])
                        root.left = left
                        root.right = right
                        res.append(root)
        return res


# Simple version.
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nums = [i for i in range(1, n + 1)]
        if nums:
            return self.generateTreesHelp(nums)
        else:
            return []
        
        
    def generateTreesHelp(self, nums):
        res = []
        if len(nums) <= 0:
            return [None]
        if len(nums) == 1:
            return [TreeNode(nums[0])]
        for i in range(len(nums)):
            leftSub = self.generateTreesHelp(nums[:i])
            rightSub = self.generateTreesHelp(nums[i+1:])
            for left in leftSub:
                for right in rightSub:
                    root = TreeNode(nums[i])
                    root.left = left
                    root.right = right
                    res.append(root)
        return res