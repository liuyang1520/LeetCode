"""
Note it is unicode, not str
"""
class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            newS = S.lower()
            firstName, rest = newS.split('@')
            return "{}@{}".format(firstName[0] + '*'*5 + firstName[-1], rest)
        else:
            newS = filter(unicode.isdigit, S)
            if len(newS) == 10:
                return "***-***-{}".format(newS[-4:])
            else:
                return "+{}-***-***-{}".format('*'*(len(newS) - 10), newS[-4:])
