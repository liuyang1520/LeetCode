"""
Each time step *= -2, and reverse the order
"""
class Solution(object):
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        count, left, right, step = 0, 1, n, 2
        while count < n-1:
            if step > 0:
                # for i in range(left, right+1, step):
                #     count += 1
                count += (right - left) / step + 1
                i = left + ((right - left) / step) * step
                if i == right: right -= step/2
                left += step/2
            else:
                # for i in range(right, left-1, step):
                #     count += 1
                count += (right - left) / abs(step) + 1
                i = right + ((right - left) / abs(step)) * step
                if i == left: left -= step/2
                right += step/2
            step = -2 * step
        return right if step < 0 else left