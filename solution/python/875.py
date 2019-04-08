"""
@difficulty: medium
@tags: binary search
@notes: Solution 1 uses greedy to try to optimize piles to the average, however, it fails in some cases.
Solution 2 uses binary search to iterate all possible K within [1, max(piles)].
Solution 3 refactor the `ceil` in solution 2 to (i + mid - 1)/mid for better performance.
"""
class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        from math import ceil
        piles.sort(reverse=True)
        average = int(ceil(sum(piles) / float(H)))
        H -= len(piles)
        for i in range(len(piles)):
            if H <= 0:
                break
            needs = min(int(ceil(piles[i] / float(average))) - 1, H)
            if needs > 0:
                H -= needs
                piles[i] = int(ceil(piles[i] / float(needs + 1)))
        return max(piles)


class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        from math import ceil
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) / 2
            if sum(int(ceil(i/float(mid))) for i in piles) <= H:
                right = mid - 1
            else:
                left = mid + 1
        return left


class Solution(object):
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        from math import ceil
        left, right = 1, max(piles)
        while left <= right:
            mid = (left + right) / 2
            if sum((i + mid - 1)/mid for i in piles) <= H:
                right = mid - 1
            else:
                left = mid + 1
        return left
