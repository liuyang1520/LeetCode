"""
Brute-force
"""
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        import math
        res = []
        temp = S.replace('-', '').upper()[::-1]
        for i in range(int(math.ceil(len(temp) * 1.0 / K))):
            res.append(temp[i*K: min(len(temp), i*K + K)])
        return "-".join(res)[::-1]
