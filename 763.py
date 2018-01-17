"""
Iterate through all values, use two counter to judge whether all current letters are in global counter.
As only 26 letter at most, so O(26*n)

Another solution would be going throught the list first to track the min/max index of each letter, then go through the whole list again
"""
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        from collections import Counter
        counter = Counter(S)
        temp = Counter()
        lastIndex = -1
        res = []
        for i in range(len(S)):
            temp[S[i]] += 1
            if all([temp[key] == counter[key] for key in temp]):
                res.append(i - lastIndex)
                temp = Counter()
                lastIndex = i
        return res
