# Sort the strings order by len. Brute-force from the shortest string.
# Solution2: calculate the longest common length from the first to the rests, then pick up the smallest value.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs = sorted(strs, key = lambda x: len(x))
        if not strs[0]:
            return ""
        for i in range(len(strs[0]) - 1, -1, -1):
            j = 0
            while j < len(strs):
                if not strs[j].startswith(strs[0][:i+1]):
                    break
                j += 1
            if j == len(strs):
                return strs[0][:i+1]
        return ""