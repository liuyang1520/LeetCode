# DFS problem, recursive solution.
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums = digits
        self.dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        print nums
        return self.letterCombinationsHelper(nums)
        
        
    def letterCombinationsHelper(self, inputDigits):
        if not inputDigits:
            return []
        res = []
        sub = self.letterCombinationsHelper(inputDigits[1:])
        for i in self.dict[inputDigits[0]]:
            if not sub:
                res += [i]
            else:
                for j in sub:
                    res += [i + j]
        return res