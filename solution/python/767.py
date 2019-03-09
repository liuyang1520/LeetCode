"""
Sort the counter by count, then assemble the result by picking separating it into two lists.
Or use the greedy algorithm to always pick up the most frequent value.
"""
class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        """
        from collections import Counter
        counter = Counter(S)
        if max(counter.values()) * 2 > len(S) + 1:
            return ''
        sortedCounter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        temp = []
        for value, count in sortedCounter:
            temp += [value] * count
        res = []
        for i in range(len(temp) / 2):
            res += [temp[i], temp[i + len(temp) / 2 + len(temp) % 2]]
        if len(temp) % 2:
            res += [temp[len(temp) / 2]]
        return "".join(res)
