"""
Sliding window:
if end - start > k + most_common_cha_times:
    then we should move the start + 1
Note, we need to use a while loop, since most_common_cha_times may decrease when we move, which incurs positive regeneration.
"""
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import Counter
        start, res, counter = 0, 0, Counter()
        for i in range(len(s)):
            counter[s[i]] += 1
            maxCount = counter.most_common(1)[0][1]
            while i - start + 1 > k + maxCount:
                counter[s[start]] -= 1
                start += 1
            res = max(res, i - start + 1)
        return res