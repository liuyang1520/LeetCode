# Use a stack to trace the values
# Take care of the edge cases
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.replace("//", "/")
        path = path.split("/")
        stack = []
        for i in path:
            if i:
                if i != "." and i != "..":
                    stack.append(i)
                elif i == ".." and len(stack):
                    stack.pop()
        return "/" + "/".join(stack)