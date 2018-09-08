"""
DFS with memory dictionary.
Might a little overkill to transform the data many times in the middle. Should be improved by building the helper directly.
"""
class Solution(object):
    def loudAndRich(self, richer, quiet):
        """
        :type richer: List[List[int]]
        :type quiet: List[int]
        :rtype: List[int]
        """
        quietest = []
        from collections import defaultdict
        richerDict = defaultdict(set)
        for x, y in richer:
            richerDict[y].add(x)
            if richerDict[x]:
                richerDict[y] |= richerDict[x]
        quietest = {}
        def helper(index):
            if index in quietest:
                return quietest[index]
            quietest[index] = quiet[index]
            for i in richerDict[index]:
                if i in quietest:
                    quietest[index] = min(quietest[index], quietest[i])
                else:
                    quietest[index] = min(quietest[index], helper(i))
            return quietest[index]

        for i in range(len(quiet)):
            helper(i)
        reverseMap = {val: i for i, val in enumerate(quiet)}
        return map(lambda x: reverseMap[x[1]], sorted(quietest.items(), key=lambda x: x[0]))
