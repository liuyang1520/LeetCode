"""
Use stats to record the location as a dictionary
"""
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        stats = {}
        for i in range(len(S)):
            char = S[i]
            if char not in stats:
                stats[char] = [i]
            else:
                stats[char].append(i)
        res = []
        for i in range(len(S)):
            char = S[i]
            minDistance = float('inf')
            for j in stats[C]:
                minDistance = min(minDistance, abs(i - j))
            res.append(minDistance)
        return res
