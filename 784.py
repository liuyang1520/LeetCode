"""
DFS
"""
class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        results = set([S])
        def helper(s, index):
            if index >= len(s):
                return
            if s[index].isalpha():
                upper = s[:index] + s[index].upper() + s[index+1:]
                lower = s[:index] + s[index].lower() + s[index+1:]
                results.add(upper)
                results.add(lower)
                helper(upper, index+1)
                helper(lower, index+1)
            else:
                helper(s, index+1)
        helper(S, 0)
        return list(results)
