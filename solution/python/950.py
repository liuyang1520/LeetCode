"""
@difficulty: medium
@tags: misc
@notes: 1. recursion, divide sorted deck into 2 halfs, run deckRevealedIncreasing on the second half, and combines 2 halfs together.
2. Simulate the process with deck index.
"""
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort()
        length = len(deck)
        if length <= 1:
            return deck
        half = length / 2 + length % 2
        res = [0] * length
        temp = self.deckRevealedIncreasing(deck[half:])
        if length % 2:
            temp = temp[-1:] + temp[:-1]
        for i in range(length):
            if i % 2 == 0:
                res[i] = deck[i/2]
            else:
                res[i] = temp[(i-1)/2]
        return res
