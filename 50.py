# Need to discuss n > 0, n < 0, n = 0, x = 1, x = -1.
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        res = 1
        if x == 1:
            return res
        if x == -1:
            return [1, -1][n % 2]
        if n < 0:
            i = 0
            while i < -n:
                res *= 1.0/x
                if abs(res - 0) < 0.0000000001:
                    break
                i += 1
        elif n > 0:
            i = 0
            while i < n:
                res *= x
                if abs(res - 0) < 0.0000000001:
                    break
                i += 1
        else:
            res = 1
        return res


# Find a recursive solution online, which is much faster than mine. http://www.cnblogs.com/zuoyuan/p/3773182.html.
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        elif n < 0:
            return 1 / self.myPow(x, -n)
        elif n % 2:
            return self.myPow(x*x,n/2)*x
        else:
            return self.myPow(x*x,n/2)