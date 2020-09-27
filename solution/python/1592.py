"""
@difficulty: easy
@tags: misc
@notes: count the spaces then build the string based on the calculation
"""
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = list(filter(bool, text.split(" ")))
        length = len(text) - sum(len(word) for word in words)
        if len(words) == 1:
            return words[0] + " " * length
        div = len(words) - 1
        splitter = (length // div) * " "
        end = (length % div) * " "
        return splitter.join(words) + end
