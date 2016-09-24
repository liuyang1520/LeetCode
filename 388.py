# https://discuss.leetcode.com/topic/55097/simple-python-solution
# Very elegant solution
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        longestPathLength = 0
        pathLength = {}
        for line in input.split("\n"):
            path = line.lstrip("\t")
            depth = len(line) - len(path)
            if "." in path:
                longestPathLength = max(longestPathLength, pathLength.get(depth, 0) + len(path))
            else:
                pathLength[depth + 1] = pathLength.get(depth, 0) + len(path) + 1
        return longestPathLength