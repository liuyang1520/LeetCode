"""
Use a set to track friend number that is already in circle.
Similar to DFS
"""
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        friendSet = set()
        length = len(M)
        res = 0
        for i in range(length):
            stack = []
            if i not in friendSet:
                res += 1
                stack.append(i)
                friendSet.add(i)
            while stack:
                k = stack.pop()
                for j in range(length):
                    if M[k][j] and j not in friendSet:
                        stack.append(j)
                        friendSet.add(j)
        return res
