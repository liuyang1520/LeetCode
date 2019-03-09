"""
Use bfs to split parentheses level by level:
()())()
L1: )())(), (())()...
L2 will not be reached since there is already valid string found in level 1
Once we found the maximun length of string, we don't go further
"""
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValidString(inputString):
            count = 0
            for i in inputString:
                if i == "(":
                    count += 1
                elif i == ")":
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
            
        queue, visited, foundMaxNumberOfPairs, res = [s], set([s]), False, []
        while queue:
            temp = queue.pop(0)
            if isValidString(temp):
                foundMaxNumberOfPairs = True
                res.append(temp)
            elif not foundMaxNumberOfPairs:
                for i in range(len(temp)):
                    if temp[i] in "()":
                        t = temp[:i] + temp[i+1:]
                        if t not in visited:
                            queue.append(t)
                            visited.add(t)
        return res