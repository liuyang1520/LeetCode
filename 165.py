# Edge cases:
# 1.0, 1
# 1.15, 1.9
# 01, 1
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        c1, c2 = version1.count("."), version2.count(".")
        for i in range(abs(c1 - c2)):
            if c1 > c2:
                version2 += ".0"
            else:
                version1 += ".0"
        t1, t2 = version1.split("."), version2.split(".")
        for i in range(len(t1)):
            if int(t1[i]) == int(t2[i]):
                if i == len(t1) - 1:
                    return 0
            else:
                return (-1, 1)[int(t1[i]) > int(t2[i])]