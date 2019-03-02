# If "+, -", handle it; if "*, /", merge it.
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import re
        s = re.sub(r"\d+", r" \g<0> ", s)
        s = s.split()
        pos = 0
        res = 0
        prev = 1
        temp = 0
        while pos < len(s):
            if s[pos] == "+" or s[pos] == "-":
                res += temp * prev
                prev = 1 if s[pos] == "+" else -1
            elif s[pos] == "*":
                temp = temp * int(s[pos + 1])
                pos += 1
            elif s[pos] == "/":
                temp = temp / int(s[pos + 1])
                pos += 1
            else:
                temp = int(s[pos])
            pos += 1
        res += temp * prev
        return res