"""
Build the output string
"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.getOutput(S) == self.getOutput(T)

    def getOutput(self, inputString):
        output = []
        for i in inputString:
            if i == "#":
                if output: output.pop()
            else:
                output.append(i)
        return "".join(output)
