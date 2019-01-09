"""
As long as a number appears on both front and back, the number is not valid anymore.
"""
class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        numbers = set(fronts).union(set(backs))
        dups = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                dups.add(fronts[i])
        res = numbers - dups
        if res:
            return min(res)
        return 0
