# http://bookshadow.com/weblog/2016/11/08/leetcode-poor-pigs/
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        import math
        return int(math.ceil(math.log(buckets, minutesToTest/minutesToDie + 1)))