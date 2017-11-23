"""
1. TLE
2. Accepted
Only need to calculate until reach n, so solution 1 wastes some time.
"""
class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
       #1   22  11  2   1   22  1   22  11  2   11  22  1   2   11  2   1   22  11  2   11  2   1   22  1   22  11  2   1   22
       #1   2   2   1   1   2   1   2   2   1   2   2   1   1   2   1   1   2   2   1   2   1   1   2   1   2   2   1   1   2   1   1
       #122112122 | 1221121122121 | 1212211211
        if n == 0:
            return 0
        if n <= 2:
            return 1
        nums = [2]
        prev = 2
        length = 2
        count = 1
        while length < n:
            temp = nums.pop(0)
            current = 2 if prev == 1 else 1
            nums.extend([current] * temp)
            prev = current
            length += 1
            if temp == 1:
                count += 1
        return count

class Solution(object):
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1, 2, 2]
        prev = 2
        i = 2
        while len(nums) <= n:
            temp = nums[i]
            current = 2 if prev == 1 else 1
            nums.extend([current] * temp)
            prev = current
            i += 1
        return nums[:n].count(1)
