"""
@difficulty: hard
@tags: DFS
@notes: DFS to iterate all possible combinations, calculate the score map and counter for each word for speeding purpose.
"""
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        from collections import Counter
        self.maxScore = 0
        scoreMap = dict([[chr(i+97), score[i]] for i in range(0, 26)])
        wordsScore = []
        for word in words:
            subtotal = 0
            for char in word:
                subtotal += scoreMap[char]
            wordsScore.append([Counter(word), subtotal])
        def dfs(wordsScore, counter, score):
            if score > self.maxScore:
                self.maxScore = score
            if not wordsScore:
                return
            for i, (wordCounter, wordScore) in enumerate(wordsScore):
                if len(wordCounter - counter) > 0:
                    continue
                dfs(wordsScore[i+1:], counter - wordCounter, score + wordScore)
        dfs(wordsScore, Counter(letters), 0)
        return self.maxScore
