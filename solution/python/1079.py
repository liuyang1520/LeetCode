"""
@difficulty: easy
@tags: dfs, math
@notes: Recursive solution, can be improved with only passing the counts of each char, or using math calculations.
"""
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        uniq = set()
        def helper(cur, rest):
            uniq.add(cur)
            for i in range(len(rest)):
                helper(cur + rest[i], rest[:i] + rest[i+1:])
        helper("", tiles)
        return len(uniq) - 1
