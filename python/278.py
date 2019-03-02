# Binary search
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        if isBadVersion(1):
            return 1
        while left <= right:
            mid = (left + right) / 2
            if mid > 1 and isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            if mid > 1 and isBadVersion(mid) and isBadVersion(mid - 1):
                right = mid - 1
            elif (mid > 1 and not isBadVersion(mid) and not isBadVersion(mid - 1)) or (mid == 1 and not isBadVersion(mid)):
                left = mid + 1

# Found that the following version works too
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = (left + right) / 2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left