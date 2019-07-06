"""
@difficulty: easy
@tags: misc
@notes: The problem description is misleading, actually it counts the diff of itself and sorted array.
"""
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return sum(heights[i] != val for i, val in enumerate(sorted(heights)))
