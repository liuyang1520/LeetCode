# Need to consider many edge cases
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if not denominator:
            return ""
        nega = False
        if numerator * denominator < 0:
            nega = True
            numerator, denominator = abs(numerator), abs(denominator)
        res = []
        fractionDict = {}
        pos, count = 0, 0
        hasLoop = False
        while 1:
            quotient, numerator = numerator / denominator, 10 * (numerator % denominator)
            res += [quotient]
            pos += 1
            count += 1
            if numerator == 0:
                break
            if numerator not in fractionDict:
                fractionDict[numerator] = pos
            else:
                pos = fractionDict[numerator]
                hasLoop = True
                break
        if nega:
            res[0] = "-" + str(res[0])
        if len(res) == 1:
            return str(res[0])
        else:
            res[0] = str(res[0]) + "."
        if not hasLoop:
            return "".join(map(str, res))
        else:
            return "".join(map(str, res[:pos])) + "(" + "".join(map(str, res[pos:count])) + ")"