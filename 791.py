"""
First make the letters of the new string using S, then add the letters from T that doesn't appear in S
"""
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        from collections import Counter
        counter = Counter(T)
        results = ""
        for i in S:
            if i in counter:
                results += i * counter[i]
        for i in counter:
            if i not in results:
                results += i * counter[i]
        return results
