"""
DFS solution
"""
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        def helper(data, index, word, wordList):
            # generate a list of "XXX" for a list of combinations of letters: [set'XY', set'KZ', set'ABC'...]
            if len(data) == len(word):
                wordList.append(word)
                return
            for i in data[index]:
                helper(data, index+1, word + i, wordList)

        def dfs(bottom):
            # dfs part with memorization
            if len(bottom) == 2:
                if bottom in allowedDict:
                    return True
                return False
            nextBottom = []
            for i in range(len(bottom)-1):
                if bottom[i:i+2] not in allowedDict:
                    return False
                nextBottom.append(allowedDict[bottom[i:i+2]])
            wordList = []
            helper(nextBottom, 0, "", wordList)
            for word in wordList:
                if word not in backtrackFail:
                    if dfs(word):
                        return True
                    else:
                        backtrackFail.add(word)
            return False

        allowedDict = {}
        for word in allowed:
            if word[:2] not in allowedDict:
                allowedDict[word[:2]] = set([word[2]])
            else:
                allowedDict[word[:2]].add(word[2])
        backtrackFail = set()
        return dfs(bottom)
