"""
@difficulty: medium
@tags: DFS, tree
@notes: Solution 1 runs two DFS to get the nodes count and total coins for each subtree, then sum the count - coins.
Solution 2 combines the two DFS into a single one.
"""
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0
            count, coins = 1, root.val
            if root.left:
                lcount, lcoins = dfs(root.left)
                count += lcount
                coins += lcoins
            if root.right:
                rcount, rcoins = dfs(root.right)
                count += rcount
                coins += rcoins
            root.count = count
            root.coins = coins
            return count, coins
        dfs(root)
        res = [0]
        def helper(root):
            if not root:
                return
            if root.left:
                res[0] += abs(root.left.count - root.left.coins)
                helper(root.left)
            if root.right:
                res[0] += abs(root.right.count - root.right.coins)
                helper(root.right)
        helper(root)
        return res[0]


class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root:
                return 0, 0
            count, coins = 1, root.val
            if root.left:
                lcount, lcoins = dfs(root.left)
                count += lcount
                coins += lcoins
            if root.right:
                rcount, rcoins = dfs(root.right)
                count += rcount
                coins += rcoins
            self.res += abs(count - coins)
            return count, coins
        self.res = 0
        dfs(root)
        return self.res
