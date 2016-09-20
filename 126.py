"""
Get TLE if directly use BFS.
The solution construct the graph at first, then do the BFS.
Note, updating the visited set should be done after all nodes in this level of depth are visited.
"""
# TLE
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        queue = [(beginWord, 1, [beginWord])]
        shortestPathLength = 100000
        res = []
        while queue:
            lastWord, length, trace = queue.pop(0)
            if length >= shortestPathLength:
                break
            for i in range(len(lastWord)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    newWord = lastWord[:i] + j + lastWord[i+1:]
                    if newWord == endWord:
                        shortestPathLength = length + 1
                        res.append(trace + [newWord])
                    if newWord != lastWord and newWord in wordlist and newWord not in trace:
                        queue.append((newWord, length + 1, trace + [newWord]))
        return res


class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        # construct graph
        graph = {}
        wordlist.update(set([beginWord, endWord]))
        for i in wordlist: graph[i] = []
        for word in graph:
            for j in range(len(beginWord)):
                for k in "abcdefghijklmnopqrstuvwxyz":
                    node = word[:j] + k + word[j+1:]
                    if node in wordlist: graph[word] += [node]
        
        # BFS
        queue = [[beginWord]]
        notReachShortestLength, visited = True, set()
        res = []
        while notReachShortestLength and queue:
            temp = set()
            for i in range(len(queue)):
                trace = queue.pop(0)
                for node in graph[trace[-1]]:
                    if node == endWord:
                        res.append(trace + [node])
                        notReachShortestLength = False
                    elif node not in visited:
                        queue.append(trace + [node])
                        temp.add(node)
            visited.update(temp)
        return res