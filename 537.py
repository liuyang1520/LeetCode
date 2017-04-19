class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int1, int2 = a.split('+'), b.split('+')
        x1, y1 = int(int1[0]), int(int1[1][:-1])
        x2, y2 = int(int2[0]), int(int2[1][:-1])
        
        x = x1 * x2 - y1 * y2
        y = x1 * y2 + x2 * y1
        
        return str(x) + "+" + str(y) + "i"