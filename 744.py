"""
Brute-force
"""
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        for i in letters:
            if i > target:
                return i
        return letters[0]
