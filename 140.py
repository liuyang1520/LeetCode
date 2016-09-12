# DFS, Time Limit Exceeded
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        def wordBreakHelper(sentence, restStr):
            if not restStr:
                res.append(sentence)
                return
            for i in wordDict:
                if restStr.startswith(i):
                    wordBreakHelper(sentence + (" " if sentence else "") + i, restStr[len(i):])
            
        res = []
        wordBreakHelper("", s)
        return res


# DP, store partial solution, Memory Limit Exceeded
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        dp = [[] for i in range(len(s) + 1)]
        dp[0] = [""]
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    for k in dp[j]:
                        dp[i].append((k + " " + s[j:i]) if k else s[j:i])
        return dp[-1]


# DFS with pruning operations
# sentenceDict stores the calculated results for further usage
# http://bookshadow.com/weblog/2015/07/21/leetcode-word-break-ii/
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        sentenceDict = {}
        def wordBreakHelper(restStr):
            sentences = []
            if restStr in wordDict:
                sentences.append(restStr)
            for i in range(1, len(restStr)):
                part1, part2 = restStr[:i], restStr[i:]
                if part1 in wordDict:
                    if part2 in sentenceDict:
                        temp = sentenceDict[part2]
                    else:
                        temp = wordBreakHelper(part2)
                else:
                    continue
                for sentence in temp:
                    sentences.append(part1 + " " + sentence)
            sentenceDict[restStr] = sentences
            return sentences
            
        return wordBreakHelper(s)