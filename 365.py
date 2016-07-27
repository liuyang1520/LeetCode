# If z is multiple of gcd(x, y), then it is fine.
# Same idea with better implementation here, https://www.hrwhisper.me/leetcode-water-jug-problem/
class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x > y:
            x, y = y, x
        if z == 0:
            return True
        if x < 1:
            return False
        gcd = 1
        for i in range(2, x + 1):
            if x % i == 0 and y % i == 0:
                gcd = i
        if gcd == 1 and z <= (y + x):
            return True
        if z <= (y + x) and z % gcd == 0:
            return True
        return False