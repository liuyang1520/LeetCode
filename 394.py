"""
Use a stack to store values, whenever "]" comes in, transfrom d[abc] in to abcabc...
"""
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        pos, posStack = 0, 0
        while pos < len(s):
            if s[pos] != "]":
                stack.append(s[pos])
                posStack += 1
            else:
                j = posStack - 1
                while j >= 0 and stack[j] != "[":
                    j -= 1
                num = ""
                k = j - 1
                while k >= 0 and '0' <= stack[k] <= '9':
                    k -= 1
                num = int("".join(stack[k+1:j]))
                stack = stack[:k+1] + ["".join(stack[j+1:posStack]) * num]
                posStack = k + 2
            pos += 1
        return "".join(stack)