"""
Find the most frequent one X, then there are only two conditions:
1. if the empty slots between two X, can be filled with other chars, then do it in this way;
2. if not, then it means that all tasks can be done without idle time.
For example:
AAA BBB CC, n=2 => ABC ABC AB
AAA BBB CC, n=1 => ABC ABC AB
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        counter = Counter(tasks)
        maxKey, maxValue = counter.most_common(1)[0]
        total = len(tasks)
        if maxValue * n >= total - maxValue:
            return (n+1) * (maxValue - 1) + counter.values().count(maxValue)
        else:
            return total
