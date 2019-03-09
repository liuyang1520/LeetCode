"""
Group the rabbits into i + 1, if more than i + 1, then need another (i + 1) rabbits in another group
"""
class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        from collections import Counter
        counter = Counter(answers)
        res = 0
        for i in counter:
            div, remainder = counter[i] / (i + 1), 1 if counter[i] % (i + 1) else 0
            res += (div + remainder) * (i + 1)
        return res
