# dictionary + sort
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        counter = Counter(s)
        rank = sorted(counter.items(), key= lambda x: x[1], reverse = True)
        res = ""
        for i in rank:
            res += i[0] * i[1]
        return res