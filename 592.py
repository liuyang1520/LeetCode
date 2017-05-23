"""
Use fraction module and is_integer() method
"""
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        from fractions import Fraction

        if expression[0] != '-':
            expression = '+' + expression
        expression = expression + '+'
        res = 0
        start = 0
        for i in range(1, len(expression)):
            if expression[i] in "+-":
                res += Fraction(expression[start:i])
                start = i

        return str(res) + '/1' if float(res).is_integer() else str(res)
