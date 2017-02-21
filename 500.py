"""
1. compare the words to each row iteratively;
2. push to the result.
"""
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for word in words:
            wordLower = word.lower()
            temp = ""
            for row in rows:
                if wordLower[0] in row:
                    temp = row
                    break
            valid = True
            for letter in wordLower:
                if letter not in temp:
                    valid = False
                    break
            if valid: res.append(word)
        return res