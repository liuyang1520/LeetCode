# A recursive implementation of DP.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n == 0:
            return []
        for i in range(n):
            if (not self.generateParenthesis(i)) and (not self.generateParenthesis(n - 1 - i)):
                res.append("()")
            elif not self.generateParenthesis(n - 1 - i):
                for x in self.generateParenthesis(i):
                    res.append("(" + x + ")")
            elif not self.generateParenthesis(i):
                for y in self.generateParenthesis(n - 1 - i):
                    res.append("()" + y)
            else:
                for x in self.generateParenthesis(i):
                    for y in self.generateParenthesis(n - 1 - i):
                        res.append("(" + x + ")" + y)
        return res


# An improved DP solution.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        trace = [[] for i in range(n + 1)]
        trace[0] = [""]
        for i in range(n + 1):
            for j in range(i):
                trace[i] += ["(" + x + ")" + y for x in trace[j] for y in trace[i - 1 - j]]
        return trace[n]



# DFS, recursive solution.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generateHelper(n, n, res, "")
        return res
        
    def generateHelper(self, left, right, res, solution):
        if left == 0 and right == 0:
            res.append(solution)
        if left > 0:
            self.generateHelper(left - 1, right, res, solution + "(")
        if left < right:
            self.generateHelper(left, right - 1, res, solution + ")")