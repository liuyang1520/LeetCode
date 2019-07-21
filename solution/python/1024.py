"""
@difficulty: medium
@tags: greedy
@notes: Always picking up the max clip[1] from clips, the solution can be improved to O(nlogn) with sorting in advance.
"""
class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        cur, count, nextCur = 0, 0, 0
        flag = True
        while flag:
            flag = False
            for clip in clips:
                if clip[0] <= cur and clip[1] >= T:
                    return count + 1
                if clip[0] <= cur and clip[1] > nextCur:
                    nextCur = clip[1]
                    flag = True
            cur = nextCur
            count += 1
        return -1
