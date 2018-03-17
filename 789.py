"""
The rectangle is the area that a ghost can travel.
"""
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        xt, yt = target
        for x, y in ghosts:
            if abs(x - xt) + abs(y - yt) <= abs(xt) + abs(yt):
                return False
        return True
